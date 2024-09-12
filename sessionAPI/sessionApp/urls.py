from django.urls import path
from . import views

urlpatterns = [
    path('count/', views.page_count),
    path('displayItem/', views.display_item),
    path('index/', views.index),
    path('addItem/', views.add_item),
]