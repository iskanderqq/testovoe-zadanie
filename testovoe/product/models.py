from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    creator = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_start = models.DateField(auto_now_add=True)
    time_of_start = models.TimeField(auto_now_add=True)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    price = models.FloatField()


class Lesson(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)


