from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [

    path("", greet),
    
]