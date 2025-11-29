from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import UserAccount
from posts.models import Recipe


# ============================
# HOME PAGE
# ============================
def home(request):
    user = None

    if "user_id" in request.session:
        try:
            user = UserAccount.objects.get(id=request.session["user_id"])
        except UserAccount.DoesNotExist:
            user = None

    return render(request, "home.html", {"user": user})


# ============================
# ABOUT PAGE
# ============================
def about(request):
    return render(request, 'about.html')


# ============================
# LOGIN PAGE
# ============================
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

        # Validate password
        if not check_password(password, user.password):
            messages.error(request, "Invalid email or password.")
            return redirect("login")

        # Save into session (login)
        request.session["user_id"] = user.id
        request.session["user_name"] = user.name
        request.session["user_email"] = user.email

        messages.success(request, "Login successful!")
        return redirect("home")

    return render(request, "login.html")


# ============================
# REGISTER PAGE
# ============================
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        # Create user
        UserAccount.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")


# ============================
# LOGOUT
# ============================
def logout_view(request):
    request.session.flush()     # clears all session data
    messages.success(request, "Logged out successfully.")
    return redirect("home")


# ============================
# EDIT PROFILE
#=============================
def edit_profile(request):
    user = None
    if 'user_id' in request.session:
        try:
            user = UserAccount.objects.get(id=request.session['user_id'])
        except UserAccount.DoesNotExist:
            user = None

    if request.method == 'POST' and user:
        name = request.POST.get('name')
        email = request.POST.get('email')

        user.name = name
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': user})




# ============================
# CONTACT & CATEGORIES
# ============================
def contact(request):
    return render(request, 'contact.html')


def categories(request):
    return render(request, 'categories.html')


# ============================
# PROFILE PAGE
# ============================
def profile(request):
    # If user not logged in → redirect
    if "user_id" not in request.session:
        return redirect("login")

    # get logged in user
    user = UserAccount.objects.get(id=request.session["user_id"])

    # Example saved recipes (replace later with real saved list)
    saved = Recipe.objects.all()[:3]

    return render(request, 'profile.html', {
        "user": user,
        "saved_recipes": saved
    })
