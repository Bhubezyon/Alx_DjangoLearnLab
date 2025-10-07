from django.urls import path
from .view import NotificationListView

urlpatterns = [
    path('posts', NotificationListView.as_view(), name='notifications'),
]