from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FoodCategory, Food


def food_list(request, food_category_slug=None):
    food_category = None
    food_categories = FoodCategory.objects.all()
    foods = Food.objects.filter(available=True)
    if food_category_slug:
        food_category = get_object_or_404(FoodCategory, slug=food_category_slug)
        foods = foods.filter(food_category=food_category)
    return render(request,
                  'list.html',
                  {'food_category': food_category,
                   'food_categories': food_categories,
                   'foods': foods})


def food_details(request, id, slug):
    food = get_object_or_404(Food,
                             id=id,
                             slug=slug,
                             available=True)
    return render(request, 'detail.html', {'food': food})
