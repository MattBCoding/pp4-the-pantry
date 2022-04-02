from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import DeleteUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .utils import paginateProfiles, searchProfiles


# Create your views here.
@login_required
def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 4)
    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'profiles/profiles.html', context)


@login_required
def userProfile(request, pk):
    profile = Profile.objects.get(user=pk)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)


@login_required
def editProfile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.user == profile.user:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                try:
                    form.save()
                    id = request.user.id
                    messages.success(request, 'Profile updated')
                    return redirect('user-profile', id)
                except:
                    messages.error(request,
                                   'ERROR: Only image file types are allowed')
                    context = {'form': form}
                    return render(request,
                                  'profiles/profile_form.html', context)
        else:
            form = ProfileForm(instance=profile)
    else:
        id = request.user.id
        return redirect('user-profile', id)

    context = {'form': form}
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
                else:
                    messages.error(request, 'Incorrect email entered!')

    form = DeleteUserForm()
    context = {'form': form}
    return render(request, 'profiles/delete_user.html', context)


@login_required
def myFavourites(request, pk):
    profile = Profile.objects.get(user=pk)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/my_favourites.html', context)
