from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video', 'comment_text', 'original_comment', 'like', 'dislike']
