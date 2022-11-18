from django.urls import path
from .views import food_list, food_details


app_name = 'food'


urlpatterns = [
    path('', food_list, name='food_list'),
    path('<slug:food_category_slug>/', food_list, name='food_list_by_food_category'),
    path('<int:id>/<slug:slug>/', food_details, name='food_details')
]
