from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Project, Vote, Feedback, FacilityRequest
from .serializers import ProjectSerializer, FeedbackSerializer, FacilityRequestSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

#Custom loginview (returns json responses)
@api_view(["POST"])
@permission_classes([AllowAny])
def custom_login(request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        print(f"Login attempt: {username}, {password}")
        
        user = authenticate(username=username, password=password)
        print(user)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user) # Get/Create token
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)


# User Authentication
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """ Register a new user """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User Registered Successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @action(detail=True, methods=['post', 'get'], permission_classes = [IsAuthenticated])
    def vote(self, request, pk=None):
        """ Allow a user to vote for a project (only one vote per voting session) """
        project = get_object_or_404(Project, pk=pk, status="Voting Open")
    
        if request.method == "GET":
            # Just check if the user has already voted, without adding a new vote
            has_voted = Vote.objects.filter(user=request.user, project__status="Voting Open").exists()
            return Response({"has_voted": has_voted}, status=status.HTTP_200_OK)

        # Handling POST request (actual voting)
        if Vote.objects.filter(user=request.user, project__status="Voting Open").exists():
            return Response({"error": "You have already voted in this session."}, status=status.HTTP_400_BAD_REQUEST)

        Vote.objects.create(user=request.user, project=project)
        return Response({"message": "Vote recorded successfully."}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'], permission_classes = [IsAuthenticated])
    def active_project(self, request):
        """ Fetch the active project (if any) """
        active_project = Project.objects.filter(status="Active").first()
        if not active_project:
            return Response({"message": "No active project at the moment."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(active_project)
        return Response(serializer.data)


# Facility request ViewSet
class FacilityRequestViewSet(viewsets.ModelViewSet):
    queryset = FacilityRequest.objects.all()
    serializer_class = FacilityRequestSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    
    def update(self, request, *args, **kwargs):
        """ Prevent users from updating the status field """
        instance = self.get_object()
        if "status" in request.data and not request.user.is_staff:
            return Response({"error": "You cannot update the status."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().update(request, *args, **kwargs)   
    # Filtering requests by user
    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:
            return FacilityRequest.objects.all()
        else:
            return FacilityRequest.objects.filter(user=user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # facility_request = FacilityRequest.objects.create(user=request.user, category=request.data["category"], description=request.data["description"])
        # return Response(FacilityRequestSerializer(facility_request).data, status=status.HTTP_201_CREATED)

# Feedback ViewSet
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        """ Allow citizens to submit feedback for an active project or a completed facility request """
        project_id = request.data.get("project")
        facility_request_id = request.data.get("facility_request")
        
        # Checking if feedback is for a project
        if project_id:
            project = get_object_or_404(Project, pk=project_id, status="Active")
            if Feedback.objects.filter(user=request.user, project=project).exists():
                return Response({"error": "You have already submitted feedback for this project."}, status=status.HTTP_400_BAD_REQUEST)
            feedback = Feedback.objects.create(user=request.user, project=project, rating=request.data["rating"], comments=request.data["comments"])
            
        # Checking if the feedback is for a facility request
        elif facility_request_id:
            facility_request = get_object_or_404(FacilityRequest, pk=facility_request_id, status="Completed")
            if Feedback.objects.filter(user=request.user, facility_request=facility_request).exists():
                return Response({"error": "You have already submitted feedback for this facility request."}, status=status.HTTP_400_BAD_REQUEST)
            feedback = Feedback.objects.create(user=request.user, facility_request=facility_request, rating=request.data["rating"], comments=request.data["comments"])
        
        else:
            return Response({"error": "Feedback must be linked to either an active project or a completed facility request."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(FeedbackSerializer(feedback).data, status=status.HTTP_201_CREATED)
    