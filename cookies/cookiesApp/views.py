from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm

# Create your views here.
def create_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("Home Page")

def remove_cookie(request):
    if request.session.test_cookie_worked():
        print("Cookie worked")
        request.session.delete_test_cookie()
        print("Cookie deleted")
    
    return HttpResponse("remove cookie")

def counter_cookie(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count']) + 1
    else:
        count = 1
    response = render(request, 'cookiesApp/count.html', {'count': count})
    response.set_cookie('count', count)
    return response

def index(request):
    return render(request, 'cookiesApp/index.html')

def add_item(request):
    form = ItemForm()
    response = render(request, 'cookiesApp/addItem.html', {'form': form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 120)
    return response

def display_cart(request):
    return render(request, 'cookiesApp/displayItems.html')