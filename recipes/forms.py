# from django.forms import ModelForm
from django import forms
from .models import Ingredient, Recipe, Step


class RecipeForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'featured_image',
            'youtube_link'
            ]

        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)


class IngredientForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'

    class Meta:
        model = Ingredient
        fields = [
            'ingredient',
            'quantity'
        ]


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = [
            'step'
        ]
