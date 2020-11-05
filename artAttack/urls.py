from artAttack.views import ArtDetailApi, ArtList
from django.urls.conf import path

urlpatterns = [
    path('', ArtList.as_view()),
    path("<int:id>", ArtDetailApi.as_view()),
]