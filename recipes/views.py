from distutils import command
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from .models import Profile, Recipe, Step, Ingredient
from .utils import searchRecipes
from .forms import IngredientForm, RecipeForm, StepForm


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
    form = RecipeForm(request.POST or None, request.FILES or None)
    IngredientFormset = modelformset_factory(
        Ingredient,
        form = IngredientForm,
        extra = 1
        )
    StepFormset = modelformset_factory(
        Step,
        form = StepForm,
        extra = 1
        )
    ingredientQueryset = Ingredient.objects.none()
    stepQueryset = Step.objects.none()
    formsetIngredient = IngredientFormset(request.POST or None, queryset=ingredientQueryset, prefix='ingredient')
    formsetStep = StepFormset(request.POST or None, queryset=stepQueryset, prefix='step')
    context = {
        'form': form,
        'formsetIngredient': formsetIngredient,
        'formsetStep': formsetStep
    }
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if all([form.is_valid(), formsetIngredient.is_valid(), formsetStep.is_valid()]):
            displayedRecipeForm = form.save(commit=False)
            displayedRecipeForm.owner = profile
            displayedRecipeForm.save()
            for form in formsetIngredient:
                displayedIngredientForm = form.save(commit=False)
                # if displayedIngredientForm.recipe is None:
                displayedIngredientForm.recipe = displayedRecipeForm
                displayedIngredientForm.save()
            for form in formsetStep:
                displayedStepForm = form.save(commit=False)
                # if displayedStepForm.recipe is None:
                displayedStepForm.recipe = displayedRecipeForm
                displayedStepForm.save()
            print(displayedRecipeForm)
            return redirect('view-recipe', displayedRecipeForm.id)
    
    return render(request, 'recipes/recipe_form.html/', context)


@login_required
def updateRecipe(request, pk):
    owner = get_object_or_404(Profile, user=request.user)
    recipe = get_object_or_404(Recipe, pk=pk)
    # if recipe.owner == owner:
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    IngredientFormset = modelformset_factory(
        Ingredient,
        form = IngredientForm,
        extra = 0
    )
    StepFormset = modelformset_factory(
        Step,
        form = StepForm,
        extra = 0
    )
    ingredientQueryset = recipe.ingredient_set.all()
    stepQueryset = recipe.step_set.all()
    formsetIngredient = IngredientFormset(request.POST or None, queryset=ingredientQueryset)
    formsetStep = StepFormset(request.POST or None, queryset=stepQueryset)
    context = {
        'form': form,
        'formsetIngredient': formsetIngredient,
        'formsetStep': formsetStep,
        'recipe': recipe,
    }
    if all([form.is_valid(), formsetIngredient.is_valid(), formsetStep.is_valid()]):
        displayedRecipeForm = form.save(commit=False)
        displayedRecipeForm.save()
        for form in formsetIngredient:
            displayedIngredientForm = form.save(commit=False)
            # if displayedIngredientForm.recipe is None:
            displayedIngredientForm.recipe = displayedRecipeForm
            displayedIngredientForm.save()
        for form in formsetStep:
            displayedStepForm = form.save(commit=False)
            # if displayedStepForm.recipe is None:
            displayedStepForm.recipe = displayedRecipeForm
            displayedStepForm.save()
    # else:
        return redirect('view-recipe', recipe.id)
    
    return render(request, 'recipes/recipe_form.html/', context)
