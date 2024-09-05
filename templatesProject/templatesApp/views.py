from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    data = {'name':"Rahul"}
    return render(request, 'templatesApp/welcomePage.html', data)