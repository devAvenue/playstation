from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class blog(models.Model):
    url = models.CharField(max_length=1000)
    header = models.CharField(max_length=1000)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False)
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


# class basket(models.Model):
