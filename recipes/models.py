from enum import unique
from django.db import models
import uuid

from django.urls import reverse
from profiles.models import Profile
from cloudinary.models import CloudinaryField

# Create your models here.
class Recipe(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    featured_image = CloudinaryField('image', default="https://res.cloudinary.com/mattbcoding/image/upload/v1645726300/recipe-placeholder_g50h2a.jpg")
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    # ingredients = models.CharField(max_length=200, blank=True, null=True)
    # steps = models.CharField(max_length=300, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    #add tags

    def __str__(self):
        return str(self.title)

    def get_ingredients(self):
        return self.ingredient_set.all()

    def get_steps(self):
        return self.step_set.all()
    
    def get_hx_url(self):
        return reverse("view-recipe-hx", kwargs={"pk": self.id})

    def get_ingredients(self):
        return self.ingredient_set.all()

    def get_steps(self):
        return self.step_set.all()

    def get_update_url(self):
        return reverse("update-recipe", kwargs={"pk": self.id})


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.ingredient)
    
    def get_hx_edit_url(self):
        kwargs = {
            'recipe_pk': self.recipe.id,
            'pk': self.id
        }
        print('the get hx edit url function was called')
        return reverse('update-ingredient-hx', kwargs=kwargs)


class Step(models.Model):
    step = models.CharField(max_length=800, blank=False, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.step)

    def get_hx_edit_url(self):
        kwargs = {
            'recipe_pk': self.recipe.id,
            'pk': self.id
        }
        return reverse('update-step-hx', kwargs=kwargs)
