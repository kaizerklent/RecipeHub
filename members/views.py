# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserAccount
from django.contrib.auth.hashers import make_password

def home(request):
    # return HttpResponse("Welcome to the Home Page")
    return render(request, 'home.html') 

def about(request):
    # return HttpResponse("About Us Page")
    return render(request, 'about.html')

def login_view(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        # Check password match
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Prevent duplicate emails
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Save to SQLite
        UserAccount.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Account created successfully!")
        return redirect("login")
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html') 

def contact(request):
    return render(request, 'contact.html')

def categories(request):
    return render(request, 'categories.html')

def recipes(request):
    return render(request, 'recipes.html')
