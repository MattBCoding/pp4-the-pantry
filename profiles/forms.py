from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'headline',
            'bio',
            'location',
            'profile_image',
            'social_youtube',
            'social_website'
            ]

        def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class DeleteUserForm(forms.Form):
    email = forms.EmailField()
