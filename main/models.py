from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class blog(models.Model):
    url = models.CharField(max_length=1000)
    header = models.CharField(max_length=1000)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
    def __str__(self):
        return self.header



class categories(models.Model):
    name = models.CharField(max_length=1000)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name


class products(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    photo = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)

    main_page = models.CharField(max_length=1000, default='')
    description = models.TextField(default='')
    images = models.TextField(default='')
    comments = models.TextField(default='')
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return f'[{self.category.name}] {self.name}'

class cart(models.Model):
    session = models.CharField(max_length=200)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)




