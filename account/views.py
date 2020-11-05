from account.models import Profile
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView
from account.serializer import LoginSerializer, ProfileSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework import permissions


class SignupApi(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(GenericAPIView):
    serializer_class = LoginSerializer

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


class ProfileList(ListAPIView):

    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Profile.objects.all()


class ProfileDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)