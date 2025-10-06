from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/followers/', include('followers.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/messages/', include('messages.urls')),
    path('api/search/', include('search.urls')),
]