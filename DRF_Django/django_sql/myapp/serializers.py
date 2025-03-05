from rest_framework import serializers
from .models import User

# Create serializers here
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['name', 'email', 'id']