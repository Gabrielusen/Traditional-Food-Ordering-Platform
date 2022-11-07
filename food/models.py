from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='menu_images/')

    class Meta:
        ordering = ('name',)
        verbose_name = 'foodcategory'
        verbose_name_plural = 'FoodCategories'

    def __str__(self):
        return self.name
