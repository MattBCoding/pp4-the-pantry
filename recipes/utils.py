from django.db.models import Q
from .models import Recipe

def searchRecipes(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    recipes = Recipe.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__username__icontains=search_query)
    )
    return recipes, search_query