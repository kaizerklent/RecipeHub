# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Home Page")
    return render(request, 'home.html') 

def about(request):
    # return HttpResponse("About Us Page")
    return render(request, 'about.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html') 

def contact(request):
    return render(request, 'contact.html')

def categories(request):
    return render(request, 'categories.html')

def recipes(request):
    return render(request, 'recipes.html')
