from rest_framework import serializers
from thematic_pages.models import ThematicPage


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
        fields = ('id', 'title',)
