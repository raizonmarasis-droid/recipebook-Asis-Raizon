from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    # Path for the list of recipes
    path('recipes/list/', recipe_list, name='recipe_list'),
    # Path for a specific recipe detail
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
]