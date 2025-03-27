from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Vote, Feedback, FacilityRequest, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class ProjectSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        
        
    def to_representation(self, instance):
        """ Custom representation to include vote count """
        data = super().to_representation(instance)
        data["vote_count"] = Vote.objects.filter(project=instance).count()
        return data

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all_'
        

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        
        
class FacilityRequestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    feedback = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True) 
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # returning feedback if exists with each api response
    def get_feedback(self, obj):
        feedback = Feedback.objects.filter(facility_request=obj).first()
        if feedback:
            return {
                "rating": feedback.rating,
                "comments": feedback.comments
            }
        return None  # No feedback submitted yet
    
    # returning url of the uploaded image 
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request is not None:
                return request.build_absolute_uri(obj.image.url)  # Return absolute URL
            return obj.image.url
        return None  # Return None if no image uploaded
    
    class Meta:
        model = FacilityRequest
        fields = ['id', 'user', 'username', 'category', 'description', 'status', 'image', 'image_url', 'feedback', 'created_at']
        
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read', 'created_at']