from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_cookie),
    path('remove/', views.remove_cookie),
    path('counter/', views.counter_cookie),
    path('index/', views.index),
    path('displayItems/', views.display_cart),
    path('addItem/', views.add_item),
]