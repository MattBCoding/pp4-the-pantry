from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/add-recipe/', views.addRecipe, name='add-recipe'),
    path('recipes/view-recipe/<str:pk>/', views.viewRecipe, name='view-recipe'),
]
