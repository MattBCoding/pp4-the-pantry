from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import DeleteUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from recipes.models import Recipe
from .utils import paginateProfiles, searchProfiles


# Create your views here.
def profiles(request):
    # profiles = Profile.objects.all().exclude(Q(username__isnull=True)).order_by('username')
    # context = {'profiles': profiles}
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 4)
    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'profiles/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(user=pk)
    context = {'profile':profile}
    # if profile.objects.get(username):
    #     return redirect('edit-profile')
    # else:
    return render(request, 'profiles/profile.html', context)


@login_required
def editProfile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.user == profile.user:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                id = request.user.id
                messages.success(request, 'Profile updated')
                return redirect('user-profile', id)
                # path = 'profiles/profile/{id}/'
                # return redirect(reverse(path.format(id=request.user.id)))
                # return redirect(reverse('home'))
        else:
            form = ProfileForm(instance=profile)
        # form = ProfileForm(instance=profile)
        # if request.method == 'POST':
        #     form = ProfileForm(request.POST, request.FILES, instance=profile)
        #     if form.is_valid():
        #         form.save()
        #         profile = request.user.id
        #         context = {'profile':profile}
        #         return render(request, 'user-profile', context)
    else:
        id = request.user.id
        return redirect('user-profile', id)
        # path = 'profiles/profile/{id}/'
        # return redirect(reverse(path.format(id=request.user.id)))
        # return redirect(reverse('home'))    
    
    context = {'form':form}
    return render(request, 'profiles/profile_form.html', context)

@login_required
def deleteUser(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    if request.user == profile.user:
        if request.method == 'POST':
            form = DeleteUserForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['email'] == profile.user.email:
                    user = request.user
                    logout(request)
                    user.delete()
                    messages.success(request, 'Account deleted!')
                    return redirect(reverse('home'))

    form = DeleteUserForm()
    context = {'form': form}
    return render(request, 'profiles/delete_user.html', context)

@login_required
def myFavourites(request, pk):
    profile = Profile.objects.get(user=pk)
    # my_favourites = profile.get_favourited()
    # favourites = Recipe.objects.distinct(my_favourites)
    # print(favourites)
    context = {
        'profile': profile,
        # 'favourites': favourites
    }
    return render(request, 'profiles/my_favourites.html', context)