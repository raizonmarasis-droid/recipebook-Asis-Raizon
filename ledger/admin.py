from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

admin.site.register(Profile)

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]
    list_display = ('name', 'author', 'created_on', 'updated_on')
    

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Ingredient)