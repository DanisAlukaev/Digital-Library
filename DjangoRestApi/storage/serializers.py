from rest_framework import serializers
from storage.models import Upload, Tag, ThematicPage


class UploadSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization of Upload model from JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    class Meta:
        # The model class for Serializer.
        model = Upload
        # A tuple of field names to be included in the serialization.
        fields = ('id',
                  'title',
                  'user',
                  'type',
                  'date',
                  'status',
                  'innopoints',
                  'tags',
                  'link',
                  'thematic_page')
        extra_kwargs = {'user': {'required': False}}


class TagSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization from of Tag JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    class Meta:
        # The model class for Serializer.
        model = Tag
        # A tuple of field names to be included in the serialization.
        fields = ('id',
                  'name')


class ThematicPageSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization of ThematicPage model from JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    class Meta:
        # The model class for Serializer.
        model = ThematicPage
        # A tuple of field names to be included in the serialization.
        fields = ('id',
                  'name',)
