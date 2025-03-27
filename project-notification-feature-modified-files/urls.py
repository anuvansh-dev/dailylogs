from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FeedbackViewSet, FacilityRequestViewSet, UserViewSet, custom_login, NotificationViewSet
from django.contrib.auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'feedback', FeedbackViewSet, basename='feedback')
router.register(r'facility-requests', FacilityRequestViewSet, basename='facility-request')
router.register(r'users', UserViewSet)
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path("login/", custom_login, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]