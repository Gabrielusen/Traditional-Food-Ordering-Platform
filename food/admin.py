from django.contrib import admin
from .models import FoodCategory, Food


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
    prepopulated_fields = {'slug': ('name',)}


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
