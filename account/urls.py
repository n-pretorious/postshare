from account.views import LoginApi, ProfileDetailApi, ProfileList, SignupApi
from django.urls.conf import path

urlpatterns = [
    path("register", SignupApi.as_view()),
    path("login", LoginApi.as_view()),
    path('profile', ProfileList.as_view()),
    path("profile/<int:id>", ProfileDetailApi.as_view()),
]
