from django.shortcuts import render
from .models import Recipe
# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    # Make sure rating is a float (just in case)
    for r in recipes:
        r.rating = float(r.rating)
    return render(request, 'posts/recipes.html', {'recipes': recipes})