from rest_framework import serializers
from .models import Art


class ArtSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Art
        fields = ["image", "description", "user_email"]