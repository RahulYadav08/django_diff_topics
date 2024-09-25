from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseServerError

# Create your views here.
class FirstClassView(View):
    greeting_message = "Hello World!"
    def get(self, request):
        return HttpResponseServerError("My name is Waka Waka!" + self.greeting_message)