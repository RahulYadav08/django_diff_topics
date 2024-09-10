from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    print(request.body)
    return HttpResponse("Hello World!")
