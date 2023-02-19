from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=225)

class Product(models.Model):
    title = models.CharField(max_length=225)
    price = models.IntegerField()


    

