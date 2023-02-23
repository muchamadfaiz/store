from django.db import models

# Create your models here.
class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONZE)

class Collection (models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # 9999,99
    inventory = models.IntegerField
    last_update = models.DateTimeField()
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

class Order (models.Model):

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem (models.Model):
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # why define unit price here? why not in product class?
    # its because the price of the product can change over time, so we should store it at the time the product is ordered
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem (models.Model):
    quantity = models.PositiveSmallIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

