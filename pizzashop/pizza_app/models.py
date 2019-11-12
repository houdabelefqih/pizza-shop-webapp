from rest_framework.compat import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Topping(models.Model):
    topping_name = models.CharField(max_length=255)

    def __str__(self):
        return self.topping_name


class Pizza(models.Model):
    PIZZA_TYPES = (
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )
    name = models.CharField(max_length=255)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    max_toppings = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(9)])
    pizza_type = models.CharField(max_length=1, choices=PIZZA_TYPES, null=True)

    def __str__(self):
        return self.pizza_type + ":" + self.name


class CustomerOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    order_done = models.BooleanField(default=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    TAX_AMOUNT = 20.00

    def price_ttc(self):
        return self.price_ht * (1 + CartItem.TAX_AMOUNT / 100.0)

    def price_ht(self):
        return self.price_ht * self.quantity
