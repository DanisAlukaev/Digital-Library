from rest_framework import serializers
from storage.models import Upload, Tag


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


class TagIdSerializer(serializers.ModelSerializer):
    class Meta:
        # The model class for Serializer.
        model = Tag
        # A tuple of field names to be included in the serialization.
        fields = ('id')


class UploadSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization of Upload model from JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    file = serializers.FileField(max_length=None, use_url=True, required=False)
    tags = TagIdSerializer(many=True, read_only=True)

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
                  'file')
        extra_kwargs = {'user': {'required': False}}
