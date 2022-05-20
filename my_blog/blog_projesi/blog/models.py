from operator import mod
from time import time
from turtle import title
from django.db import models
from django.urls import reverse

# Create your models here.

class Post (models.Model):
    title=models.CharField(max_length=200,null=False)
    author=models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
    )
    body=models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home")
    date=models.DateField(auto_now_add=True)
    
    
class Parfume (models.Model):
    name = models.CharField(max_length=100,null=False)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.name

