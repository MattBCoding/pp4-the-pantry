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

        #     for name, field in self.fields.items():
        #         field.widget.attrs.update({'class': 'input'})


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'ingredient',
            'quantity'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(IngredientForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = [
            'step'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(StepForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
