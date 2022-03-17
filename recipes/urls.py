from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/add-recipe/', views.addRecipe, name='add-recipe'),
    path('recipes/view-recipe/<str:pk>/', views.viewRecipe, name='view-recipe'),
    path('recipes/like-recipe/<str:pk>/', views.likeRecipe, name='like-recipe'),
    path('recipes/update-recipe/<str:pk>/', views.updateRecipe, name='update-recipe'),
    path('recipes/delete-recipe/<str:pk>/', views.deleteRecipe, name='delete-recipe'),
    path('hx/view-recipe/<str:pk>/', views.viewRecipeHx, name='view-recipe-hx'),
    path('hx/view-recipe/<str:recipe_pk>/ingredient/<str:pk>/', views.updateIngredientHx, name='update-ingredient-hx'),
    path('hx/delete-recipe/<str:recipe_pk>/ingredient/<str:pk>/', views.deleteIngredientHx, name='delete-ingredient-hx'),
    path('hx/delete-recipe/<str:recipe_pk>/step/<str:pk>/', views.deleteStepHx, name='delete-step-hx'),
    path('hx/view-recipe/<str:recipe_pk>/ingredient/', views.updateIngredientHx, name='create-ingredient-hx'),
    path('hx/view-recipe/<str:recipe_pk>/step/<str:pk>/', views.updateStepHx, name='update-step-hx'),
    path('hx/view-recipe/<str:recipe_pk>/step/', views.updateStepHx, name='create-step-hx'),
]
