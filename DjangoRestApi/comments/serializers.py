from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
        Class that manages serialization and deserialization of comment model from JSON.
        It inherits from rest_framework.serializers.ModelSerializer superclass
        which automatically populates a set of fields and default validators.
     """
    class Meta:
        model = Comment
        fields = ['id',
                  'content_connected',
                  'content',
                  'author']

        extra_kwargs = {'author': {'required': False}}
