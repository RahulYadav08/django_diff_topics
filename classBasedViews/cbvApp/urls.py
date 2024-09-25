from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstClassView.as_view(greeting_message = "Hello individuals!")),
]


