from account.models import Profile
from rest_framework.views import APIView
from account.serializer import LoginSerializer, ProfileSerializer, UserSerializer
from django.shortcuts import render

# from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt

# Create your views here.


class SignupApi(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email", "")
        password = data.get("password", "")
        user = auth.authenticate(email=email, password=password)

        if user:
            auth_token = jwt.encode({"email": user.email}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {"user": serializer.data, "token": auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
