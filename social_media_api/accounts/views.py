from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from .models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": serializer.data
        })


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "bio": user.bio,
            "followers": user.followers.count()
        })



from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import FollowSerializer

CustomUser = get_user_model()

# Follow a user
class FollowUserView(generics.GenericAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user_id = self.kwargs.get("user_id")
        target_user = CustomUser.objects.get(id=target_user_id)

        if request.user == target_user:
            return Response({"error": "You cannot follow yourself."}, status=400)

        request.user.following.add(target_user)
        return Response({"success": f"You are now following {target_user.username}."})

# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user_id = self.kwargs.get("user_id")
        target_user = CustomUser.objects.get(id=target_user_id)

        request.user.following.remove(target_user)
        return Response({"success": f"You have unfollowed {target_user.username}."})

# Create your views here.
