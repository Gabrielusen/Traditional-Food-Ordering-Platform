from django.db import models
from django.urls import reverse


class FoodCategory(models.Model):
    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='menu_images/',
                              blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'foodcategory'
        verbose_name_plural = 'FoodCategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_list_by_food_category', kwargs={'slug': self.slug})


class Food(models.Model):
    food_category = models.ForeignKey(FoodCategory,
                                      related_name='food',
                                      on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=True)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='foods/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('food_details', kwargs={'id': self.id, 'slug': self.slug})
