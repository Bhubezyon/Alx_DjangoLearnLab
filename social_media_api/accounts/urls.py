from  django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUnfollowView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('follow-unfollow/<str:username>/', FollowUnfollowView.as_view(), name='follow-unfollow'),
]