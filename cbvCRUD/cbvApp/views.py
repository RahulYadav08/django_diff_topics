from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

# Create your views here.
@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    model = Student
    #default template_name is student_list.html
    #default context_object_name is student_list

@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    # default template_name is student_detail.html
    #default context_object is student

@method_decorator(login_required, name='dispatch')
class StudentCreateVIew(CreateView):
    model = Student
    fields = ("id", "firstName", "lastName", "testScore")
    # default template_name is student_form.html

@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['testScore']

@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('home')
    #confirm template is student_confirm_delete.html

    def dispatch(self, request, *args, **kwargs):
        #custom authorization logic

        if not self.custom_authorization_logic(request.user):
            return HttpResponse("You are Unauthorized to perform the action", status = 201)
        
        return super().dispatch(request, *args, **kwargs)
    
    def custom_authorization_logic(self, user):
        return user.is_authenticated and user.has_perm('cbvApp.delete_student')
