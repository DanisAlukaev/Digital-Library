from rest_framework import serializers
from storage.models import Upload, Tag, BookmarkPage


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

    def to_internal_value(self, data):
        return Tag.objects.get(id=data)


class UploadSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization of Upload model from JSON.
    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """

    file = serializers.FileField(max_length=None, use_url=True, required=False)
    tags = TagSerializer(many=True)

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
                  'thematic_page')
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        upload = Upload.objects.create(**validated_data)
        for tag_data in tags_data:
            upload.tags.add(tag_data)
        return upload

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')

        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.innopoints = validated_data.get('innopoints', instance.innopoints)
        instance.status = validated_data.get('status', instance.status)
        instance.tags.clear()
        for tag_data in tags_data:
            instance.tags.add(tag_data)
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
