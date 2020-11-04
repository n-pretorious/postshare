from account.views import LoginApi, SignupApi
from django.urls.conf import path
from . import views

urlpatterns = [path("register", SignupApi.as_view()), path("login", LoginApi.as_view())]
