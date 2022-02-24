from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

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
