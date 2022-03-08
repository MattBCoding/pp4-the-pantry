from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/add-recipe/', views.addRecipe, name='add-recipe'),
    path('recipes/view-recipe/<str:pk>/', views.viewRecipe, name='view-recipe'),
    path('recipes/update-recipe/<str:pk>/', views.updateRecipe, name='update-recipe'),
    path('recipes/delete-recipe/<str:pk>/', views.deleteRecipe, name='delete-recipe'),
]
