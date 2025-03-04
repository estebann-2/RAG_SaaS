from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Document, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for Document model.
    """
    class Meta:
        model = Document
        fields = ['id', 'user', 'conversation', 'file', 'title', 'uploaded_at', 'processed']
        read_only_fields = ['uploaded_at', 'processed']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for Conversation model.
    """
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'user', 'title', 'created_at', 'messages']
        read_only_fields = ['created_at']

    def get_messages(self, obj):
        """
        Retrieve messages associated with the conversation.
        """
        messages = Message.objects.filter(conversation=obj).order_by('timestamp')
        return MessageSerializer(messages, many=True).data


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'role', 'text', 'timestamp']
        read_only_fields = ['timestamp']
