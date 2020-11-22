from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    """
    Override built-in djoser UserCreateSerializer.
    Allows creation of a new user with specified email, password and name.
    """

    # Profile picture serializer.
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta(UserCreateSerializer.Meta):
        # The model class for Serializer.
        model = User
        # A tuple of field names to be included in the serialization.
        fields = ('id',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'mid_name',
                  'image',
                  'role',
                  'degree',
                  'course',
                  'track')
