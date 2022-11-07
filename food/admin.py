from django.contrib import admin
from .models import FoodCategory


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(FoodCategory, FoodCategoryAdmin)
