from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]

from .views import (
    CommentCreateView, CommentUpdateView, CommentDeleteView,
)

urlpatterns += [
    path("post/<int:post_pk>/comment/new/", CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]