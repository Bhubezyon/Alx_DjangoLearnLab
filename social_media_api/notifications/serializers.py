from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Notification
        fields = ['id', 'actor', 'verb', 'target', 'timestamp', 'read']