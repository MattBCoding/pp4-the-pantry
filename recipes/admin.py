from django.contrib import admin
from .models import Recipe, Ingredient, Step

# Register your models here.
class RecipeIngredient(admin.StackedInline):
    model = Ingredient
    extra = 0


class RecipeStep(admin.StackedInline):
    model = Step
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [RecipeIngredient, RecipeStep]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Step)
