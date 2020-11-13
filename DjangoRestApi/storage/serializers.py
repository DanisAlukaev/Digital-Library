from rest_framework import serializers
from storage.models import Upload


class UploadSerializer(serializers.ModelSerializer):
    """
    Class that manages serialization and deserialization from JSON.

    It inherits from rest_framework.serializers.ModelSerializer superclass
    which automatically populates a set of fields and default validators.
    """
    class Meta:
        # The model class for Serializer
        model = Upload
        # A tuple of field names to be included in the serialization
        fields = ('id',
                  'title',
                  'description',
                  'published')
