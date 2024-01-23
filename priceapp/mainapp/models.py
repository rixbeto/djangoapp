from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=500)
    price = models.FloatField() # in dollars
    status = models.CharField(max_length=20, default='set')  # set/dropped/rise


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)

