from rest_framework import serializers
from .models import image

class imageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'Description']