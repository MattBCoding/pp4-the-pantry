from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Recipe, Step, Ingredient
from .utils import searchRecipes
from .forms import RecipeForm


# Create your views here.
def home(request):
    recipes, search_query = searchRecipes(request)
    context = {
        'recipes': recipes,
        'search_query': search_query
    }
    return render(request, 'index.html/', context)

def viewRecipe(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipes/recipe_detail.html/', context)


@login_required
def addRecipe(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            #temp redirect needs updating to correct page
            id = request.user.id
            return redirect('add-recipe')
    
    context = {'form': form}
    return render(request, 'recipes/recipe_form.html/', context)
