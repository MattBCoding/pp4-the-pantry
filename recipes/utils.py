from django.db.models import Q
from .models import Recipe

def searchRecipes(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # ingredients = Ingredient.objects.filter(ingredient=True)
    # steps = Step.objects.filter
    
    recipes = Recipe.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__username__icontains=search_query)
    ).exclude(
        Q(ingredient__isnull=True) |
        Q(step__isnull=True)
        ).order_by('title')

    return recipes, search_query
