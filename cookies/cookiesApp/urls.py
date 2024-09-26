from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('add/', views.create_cookie),
    path('remove/', views.remove_cookie),
    path('counter/', views.counter_cookie),
    path('index/', views.index),
    path('displayItems/', views.display_cart),
    path('addItem/', views.add_item),
    path('api/signUP/', views.RegisterUserView.as_view(), name="sign_up"),
    path('api/login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]