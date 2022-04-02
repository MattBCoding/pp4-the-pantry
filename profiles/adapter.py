from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from profiles.models import Profile
from django.contrib.auth.models import User


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = 'profiles/profile/{id}/'
        return path.format(id=request.user.id)

    # adapter method to create a user profile when the user confirms their
    # email address. Needed for first login to take them to the profile page
    def confirm_email(self, request, email_address):
        user = User.objects.get(emailaddress=email_address)
        newUserProfile = Profile(user=user)
        newUserProfile.save()
        return super().confirm_email(request, email_address)
