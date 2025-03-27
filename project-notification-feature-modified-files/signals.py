from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import FacilityRequest, Notification

# signal to create a token when a new user is created/registered
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

# signal to create and send a notification when a facility request's status gets changed from pending
@receiver(post_save, sender=FacilityRequest)
def send_request_update_notification(sender, instance, **kwargs):
    if instance.status != "Pending":
        message = f"Your facility request (ID: {instance.id}) related to '{instance.category}' has been marked as '{instance.status}'."
        Notification.objects.create(
            user = instance.user,
            facility_request = instance,
            message = message,
        )
