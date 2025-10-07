from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notificatio.objects.filter(recipient=self.request.user).order_by('-timestamp')