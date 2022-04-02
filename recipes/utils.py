from django.db.models import Q
from .models import Recipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def searchRecipes(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    recipes = Recipe.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__username__icontains=search_query)
    ).exclude(
        Q(ingredient__isnull=True) |
        Q(step__isnull=True)
        ).order_by('title')

    return recipes, search_query


def paginateRecipes(request, recipes, results):
    page = request.GET.get('page')
    paginator = Paginator(recipes, results)
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        recipes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        recipes = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, recipes
