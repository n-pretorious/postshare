from artAttack.models import Art
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from artAttack.serializer import ArtSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class ArtList(ListAPIView):

    serializer_class = ArtSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Art.objects.all()


class ArtDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ArtSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Art.objects.filter(user=self.request.user)

