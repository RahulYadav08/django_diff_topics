from django.urls import path
from . import views

urlpatterns = [
    path('studentDetails/', views.StudentListView.as_view(), name = 'home'),
    path('<int:pk>/', views.StudentDetailView.as_view(),name = "detail"),
    path('addStudent/', views.StudentCreateVIew.as_view()),
    path('updateStudent/<int:pk>', views.StudentUpdateView.as_view()),
    path('deleteStudent/<int:pk>', views.StudentDeleteView.as_view()),
]