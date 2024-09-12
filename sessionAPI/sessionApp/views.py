from django.shortcuts import render
from . import forms

# Create your views here.
def page_count(request):
    count = request.session.get('count', 0)
    count = count+1
    request.session['count'] = count
    return render(request, 'sessionApp/count.html', {'count':count})

def index(request):
    return render(request, 'sessionApp/index.html', )


def add_item(request):
    form = forms.SessionForm()
    if request.method == 'POST':
        form = forms.SessionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            request.session[name] = quantity
    return render(request, 'sessionApp/addItem.html', {'form':form})

def display_item(request):
    return render(request, 'sessionApp/DisplayItem.html')


def remove(request):


