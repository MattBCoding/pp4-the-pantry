from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import DeleteUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
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