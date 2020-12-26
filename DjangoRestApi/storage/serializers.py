from rest_framework import serializers
from storage.models import Upload, Tag, BookmarkPage, Comment
from accounts.serializers import UserCreateSerializer
from thematic_pages.serializers import ThematicPageSerializer
import os


def getsize(size_in_bytes):
    boundary = 512000
    if size_in_bytes < boundary:
        value = round(size_in_bytes / 1024, 2)
        ext = ' Kb'
    elif size_in_bytes < boundary * 1024:
        value = round(size_in_bytes / (1024 * 1024), 2)
        ext = ' Mb'
    else:
        value = round(size_in_bytes / (1024 * 1024 * 1024), 2)
        ext = ' Gb'
    return str(value) + ext


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
        fields = ('id', 'name')

    def to_internal_value(self, data):
        return Tag.objects.get(id=data)


class CommentSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization of Comment model from JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    user = UserCreateSerializer(required=False)

    class Meta:
        # The model class for Serializer.
        model = Comment
        # A tuple of field names to be included in the serialization.
        fields = ['id',
                  'upload',
                  'user',
                  'content',
                  'date']
        extra_kwargs = {'user': {'required': False}}


class UploadSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization of Upload model from JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    user = UserCreateSerializer(required=False)

    # File serialization.
    file = serializers.FileField(max_length=None, use_url=True, required=False)
    # Multiple Tag serialization.
    tags = TagSerializer(many=True, required=False)

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
                  'file',
                  'thematic_page',
                  'rating',
                  'size',
                  'name',)
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        # Describes the process of fields deserialization for object creation.

        # Retrieve tags parameters.
        try:
            tags_data = validated_data.pop('tags')
        except Exception:
            tags_data = []

        if validated_data['type'] != 3:
            validated_data['name'] = validated_data['file'].name
            validated_data['size'] = getsize(validated_data['file'].size)

        # Create a new instance of an upload.
        upload = Upload.objects.create(**validated_data)
        # Put tags in new upload.
        for tag_data in tags_data:
            upload.tags.add(tag_data)
        return upload

    def update(self, instance, validated_data):
        # Describes the process of fields deserialization for object update.

        # Retrieve tags parameters.
        try:
            tags_data = validated_data.pop('tags')
        except Exception:
            tags_data = []

        # Update title, type, innopoints, status field.
        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.innopoints = validated_data.get('innopoints', instance.innopoints)
        instance.status = validated_data.get('status', instance.status)
        instance.thematic_page = validated_data.get('thematic_page', instance.thematic_page)
        # Clear tags field.
        instance.tags.clear()
        # Set new tags.
        for tag_data in tags_data:
            instance.tags.add(tag_data)
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.name)
        # Save upload.
        instance.save()
        return instance


class BookmarkPageSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization from of BookmarkPage JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    class Meta:
        # The model class for Serializer.
        model = BookmarkPage
        # A tuple of field names to be included in the serialization.
        fields = ('id', 'title')
