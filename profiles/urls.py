from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('edit_profile/', views.editProfile, name='edit-profile'),
    path('delete_profile/<str:pk>/', views.deleteUser, name='delete-user'),
    path('profile/favourites/<str:pk>/',
         views.myFavourites, name='my-favourites'),
]
