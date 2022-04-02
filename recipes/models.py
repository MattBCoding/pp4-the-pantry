from django.db import models
import uuid
from django.urls import reverse
from profiles.models import Profile
from cloudinary.models import CloudinaryField


# Create your models here.
def_image_one = "https://res.cloudinary.com/mattbcoding/image/upload/"
def_image_two = "v1645726300/recipe-placeholder_g50h2a.jpg"
def_image = def_image_one+def_image_two


class Recipe(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)
    owner = models.ForeignKey(Profile,
                              on_delete=models.CASCADE,
                              null=False,
                              blank=False,
                              related_name='owner')
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    featured_image = CloudinaryField('image', default=def_image)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile, related_name='recipe_likes')
    favourites = models.ManyToManyField(Profile,
                                        related_name='recipe_favourites')

    def __str__(self):
        return str(self.title)

    def get_ingredients(self):
        return self.ingredient_set.all()

    def get_steps(self):
        return self.step_set.all()

    def get_hx_url(self):
        return reverse("view-recipe-hx", kwargs={"pk": self.id})

    def get_update_url(self):
        return reverse("update-recipe", kwargs={"pk": self.id})

    def total_likes(self):
        return self.likes.count()

    def get_likes(self):
        return self.likes_set.all()

    def get_favourites(self):
        return self.favourites_set.all()


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
        return reverse('update-ingredient-hx', kwargs=kwargs)

    def get_hx_delete_url(self):
        kwargs = {
            'recipe_pk': self.recipe.id,
            'pk': self.id
        }
        return reverse('delete-ingredient-hx', kwargs=kwargs)


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

    def get_hx_delete_url(self):
        kwargs = {
            'recipe_pk': self.recipe.id,
            'pk': self.id
        }
        return reverse('delete-step-hx', kwargs=kwargs)
