from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework import status, permissions, generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny


CustomUser = get_user_model()

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permission.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = self.get_queryset().get(id=user_id)
            request.user.following.add(target_user)
            return Response({'message': f'You are now following {target_user.username}'}, status=status.HHTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HHTP_404_NOT_FOUND)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = self.get_queryset().get(id=user_id)
            request.user.following.remove(target_user)
            return Response({'mesage': f'You have unfollowed {target_user.username}'}, status=status.HHTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HHTP_404_NOT_FOUND)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.object.get(id=user_id)
            request.user.following.add(target_user)
            return Response({'message': f'You are now following {target_user.name}'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HHTP_404_NOT_FOUND)

class UnfollowUserView(APIView):
    permission_classes = [permission.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
            request.user.following.remove(target_user)
            return Response({'message': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

