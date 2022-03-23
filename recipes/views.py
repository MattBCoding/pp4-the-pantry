from wsgiref import headers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Recipe, Step, Ingredient
from .utils import searchRecipes
from .forms import IngredientForm, RecipeForm, StepForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {
            'profile': profile,
        }
    else:
        context = {}
    return render(request, 'index.html/', context)

def recipes(request):
    recipes, search_query = searchRecipes(request)
    context = {
        'recipes': recipes,
        'search_query': search_query
    }
    return render(request, 'recipes/recipes.html/', context)

def viewRecipe(request, pk):
    hx_url = reverse("view-recipe-hx", kwargs={"pk": pk})
    context = {
        'hx_url': hx_url
    }
    return render(request, 'recipes/recipe_detail.html/', context)

def viewRecipeHx(request, pk):
    if not request.htmx:
        raise Http404
    try:
        recipe = Recipe.objects.get(id=pk)
        total_likes = recipe.total_likes()
        liked = False
        favourited = False
        if request.user.is_authenticated:
            if request.user is not recipe.owner.user:
                current_user = get_object_or_404(Profile, user=request.user)
                if recipe.likes.filter(id=current_user.id).exists():
                    liked = True
                    if recipe.favourites.filter(id=current_user.id).exists():
                        favourited = True
    except:
        recipe = None
    if recipe is None:
        return HttpResponse("Not Found!")
    context = {
        'recipe': recipe,
        'total_likes': total_likes,
        'liked': liked,
        'favourited': favourited
    }
    return render(request, 'recipes/snippets/recipe_detail.html/', context)

@login_required
def likeRecipe(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    profile = get_object_or_404(Profile, user=request.user)
    liked = False
    favourited = False
    if recipe.likes.filter(id=profile.id).exists():
        if recipe.favourites.filter(id=profile.id).exists():
            recipe.favourites.remove(profile.id)
            favourited = False
        recipe.likes.remove(profile.id)
        liked = False

    else:
        recipe.likes.add(profile.id)
        liked = True
        favourited = False

    if request.htmx:
        total_likes = recipe.total_likes()
        context = {
            'recipe': recipe,
            'total_likes': total_likes,
            'liked': liked,
            'favourited': favourited,
        }
        headers = {
            'HX-Trigger':'liked',
        }
        return render(request, 'recipes/snippets/like_recipe.html/', context, headers)
    return HttpResponseRedirect(reverse('view-recipe', args=[str(pk)]))

@login_required
def favouriteRecipe(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    profile = get_object_or_404(Profile, user=request.user)
    favourited = False
    if recipe.favourites.filter(id=profile.id).exists():
        recipe.favourites.remove(profile.id)
        favourited = False
    else:
        recipe.favourites.add(profile.id)
        favourited = True
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'favourited': favourited
        }
        return render(request, 'recipes/snippets/favourite_recipe.html/', context)

    if request.htmx:
        context = {
            'recipe': recipe,
            'favourited': favourited
        }
        return render(request, 'recipes/snippets/favourite_recipe.html/', context)
    return HttpResponseRedirect(reverse('view-recipe', args=[str(pk)]))
    

@login_required
def addRecipe(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            print('FORM IS VALID -------------------------->')
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            messages.success(request, 'Your recipe was created successfully!')
            if request.htmx:
                print('REQUEST IS HTMX -------------------------->')
                headers = {
                    'HX-Redirect': recipe.get_update_url()
                }
                return HttpResponse('created', headers=headers)
            return redirect(recipe.get_update_url())      
    
    return render(request, 'recipes/create_recipe.html/', context)


@login_required
def updateRecipe(request, pk):
    # owner = get_object_or_404(Profile, user=request.user)
    recipe = get_object_or_404(Recipe, pk=pk)
    # if recipe.owner == owner:
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    new_ingredient_url = reverse('create-ingredient-hx', kwargs={'recipe_pk':recipe.id})
    new_step_url = reverse('create-step-hx', kwargs={'recipe_pk':recipe.id})
    context = {
        'form': form,
        'recipe': recipe,
        'new_ingredient_url': new_ingredient_url,
        'new_step_url': new_step_url
    }
    if form.is_valid():
        print('FORM IS VALID FROM updateRecipe------------------------->')
        form.save()
        messages.success(request, 'Your recipe was updated successfully!')

    if request.htmx:
        print('REQUEST IS HTMX FROM updateRecipe------------------------->')
        # messages.success(request, 'Your recipe was updated successfully!')
        context = context
        return render(request, 'recipes/snippets/recipe_form.html', context)
    
    return render(request, 'recipes/recipe_form.html/', context)



@login_required
def updateIngredientHx(request, recipe_pk=None, pk=None):
    if not request.htmx:
        print('Not a HTMX request -----------------> updateIngredientHx views.py')
        raise Http404
    try:
        recipe = Recipe.objects.get(id=recipe_pk)
        print(recipe)
    except:
        recipe = None
    if recipe is None:
        return HttpResponse("Not Found!")
    instance = None
    if pk is not None:
        try:
            instance = Ingredient.objects.get(recipe=recipe, id=pk)
        except:
            instance = None
    print('This instance is... ------------->')
    print(instance)
    print(pk)
    print(recipe_pk)
    form = IngredientForm(request.POST or None, instance=instance)
    url = reverse('create-ingredient-hx', kwargs={'recipe_pk':recipe.id})
    if instance:
        url = instance.get_hx_edit_url()
    print(form)
    print(url)
    context = {
        'url': url,
        'ingredientform': form,
        'ingredient': instance
    }
    
    if form.is_valid():
        print('Form is valid -------------------------->')
        ingredient = form.save(commit=False)
        if instance is None:
            ingredient.recipe = recipe
        ingredient.save()
        messages.success(request, 'Your ingredient was saved successfully!')
        context['ingredient'] = ingredient
        return render(request, 'recipes/snippets/ingredient_detail.html/', context)
    if not form.is_valid():
        # messages.error(request, 'Please complete the ingredient form.')
        print('something is wrong with the form')
    
    return render(request, 'recipes/snippets/ingredient_form.html/', context)


@login_required
def updateStepHx(request, recipe_pk=None, pk=None):
    if not request.htmx:
        print('Not a HTMX request -----------------> updateStepHx views.py')
        raise Http404
    try:
        recipe = Recipe.objects.get(id=recipe_pk)
        print(recipe)
    except:
        recipe = None
    if recipe is None:
        return HttpResponse("Not Found!")
    instance = None
    if pk is not None:
        try:
            instance = Step.objects.get(recipe=recipe, id=pk)
        except:
            instance = None
    print('This instance is... ------------->')
    print(instance)
    print(pk)
    print(recipe_pk)
    form = StepForm(request.POST or None, instance=instance)
    url = reverse('create-step-hx', kwargs={'recipe_pk':recipe.id})
    if instance:
        url = instance.get_hx_edit_url()
    print(form)
    print(url)
    context = {
        'url': url,
        'stepform': form,
        'ingredient': instance
    }
    
    if form.is_valid():
        print('Form is valid -------------------------->')
        step = form.save(commit=False)
        if instance is None:
            step.recipe = recipe
        step.save()
        messages.success(request, 'Your step was saved successfully!')
        context['step'] = step
        return render(request, 'recipes/snippets/step_detail.html/', context)
    if not form.is_valid():
        # messages.error(request, 'Please complete the step form.')
        print('something is wrong with the form')
    
    return render(request, 'recipes/snippets/step_form.html/', context)

@login_required
def deleteIngredientHx(request, recipe_pk=None, pk=None):
    try:
        ingredient = Ingredient.objects.get(recipe=recipe_pk, id=pk)
    except:
        ingredient = None
    if ingredient is None:
        if request.htmx:
            return HttpResponse("Ingredient not found!")
        raise Http404
    if request.method == 'POST':
        ingredient.delete()
        messages.success(request, 'The ingredient was deleted!')
        return_url = reverse('update-recipe', kwargs={'pk': recipe_pk})
        if request.htmx:
            print('HTMX request ----------------------------->')
            headers = {
                'HX-Redirect': return_url
            }
            return HttpResponse('', headers=headers) 
            # render(request, 'recipes/snippets/ingredient-delete-response.html', {'ingredient': ingredient})
        return redirect(return_url)
    context = {
        'ingredient': ingredient
    }

    return render(request, 'recipes/snippets/ingredient_delete.html', context)

@login_required
def deleteStepHx(request, recipe_pk=None, pk=None):
    try:
        step = Step.objects.get(recipe=recipe_pk, id=pk)
    except:
        step = None
    if step is None:
        if request.htmx:
            return HttpResponse("Step not found!")
        raise Http404
    if request.method == 'POST':
        step.delete()
        messages.success(request, 'The step was deleted!')
        return_url = reverse('update-recipe', kwargs={'pk': recipe_pk})
        if request.htmx:
            print('HTMX request ----------------------------->')
            headers = {
                'HX-Redirect': return_url
            }
            return HttpResponse('', headers=headers) 
            # render(request, 'recipes/snippets/ingredient-delete-response.html', {'ingredient': ingredient})
        return redirect(return_url)
    context = {
        'step': step
    }

    return render(request, 'recipes/snippets/step_delete.html', context)


@login_required
def deleteRecipe(request, pk):
    owner = get_object_or_404(Profile, user=request.user)
    recipe = owner.recipe_set.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'The recipe was deleted!')
        # NEED TO UPDATE DELETE REDIRECT
        # so that it redirects to appropriate place based on where the user came from
        return redirect('home')
    context = {'object': recipe}
    return render(request, 'delete_template.html', context)