from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    sub_category = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'scategory' , null = True) #its refering to himself with self
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter' , args=[self.slug])


class Product(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='products')
    category = models.ManyToManyField(Category , related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    #image = models.ImageField(upload_to='products/%Y/%m/%d')
    image = models.ImageField() # we dont need this upload_to becasue we are using AWS
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug,])