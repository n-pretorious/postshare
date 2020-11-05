from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import BookSerializer
from .models import image

class BookViewSet(viewsets.ModelViewSet):
    queryset = image.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['description']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'image created'}, status=200)

