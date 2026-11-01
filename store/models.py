from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField(null=True,blank=True)
     created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField(null=True,blank=True)
     price = models.DecimalField(max_digits=5, decimal_places=2)
     stock = models.IntegerField()
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)


class Order (models.Model):
     user =models.ForeignKey( User,on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.IntegerField()
     total_price = models.IntegerField()
     created_at = models.DateTimeField(auto_now_add=True)