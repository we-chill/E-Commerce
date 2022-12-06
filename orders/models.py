from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('N', 'New'),
        ('P', 'Paid'),
        ('S', 'Shipped'),
        ('C', 'Canceled'),
    ]
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    mobile = PhoneNumberField(null=True, blank=True)
    discount = models.PositiveSmallIntegerField(null=True, blank=True, help_text='discount percents off')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default='N')

    def __str__(self):
        if self.user is not None:
            return str(self.id) + '-' + self.user.username
        return str(self.id) + '-'


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, null=True, blank=True)
