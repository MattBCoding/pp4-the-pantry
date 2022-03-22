from contextlib import nullcontext
from re import T
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField

# Create your models here.
# allauth.account.signals.email_confirmed(request, email_address)

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='profile')
    username = models.CharField(max_length=50, blank=True, null=True)
    headline = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    profile_image = CloudinaryField('image', default="https://res.cloudinary.com/mattbcoding/image/upload/v1645611940/default-chef_x2n0oe.png")
    social_youtube = models.URLField(max_length=200, blank=True, null=True)
    social_website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.username)

    def get_liked(self):
        return self.recipe_likes.all()
    
    def get_favourited(self):
        return self.recipe_favourites.all()
