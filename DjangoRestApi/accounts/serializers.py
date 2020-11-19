from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    """
    Override built-in djoser UserCreateSerializer.
    Allows creation of new user with specified email, password and name.
    """
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'mid_name', 'image', 'role', 'degree', 'course',
                  'track')
