from rest_framework.compat import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
    pizza_type = models.CharField(max_length=1, choices=PIZZA_TYPES, default='R')

    def __str__(self):
        return "{pizza_type} : {pizza_name}".format(pizza_type=self.get_pizza_type_display(), pizza_name=self.name)


class CartItem(models.Model):

    PIZZA_SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_size = models.CharField(max_length=1, choices=PIZZA_SIZES, null=True)
    toppings = models.ManyToManyField(Topping)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    subtotal= models.DecimalField(max_digits=50, decimal_places=2, default=77.77)

    def save(self, *args, **kwargs):

        # if len(self.toppings) > self.pizza.max_toppings:
        #     raise ValidationError('You cannot exceed {max_toppings} for this pizza').format(max_toppings=self.pizza.max_toppings)
        #
        # else:
        if self.pizza_size == 'S':
            self.price = self.pizza.small_price

        elif self.pizza_size == 'L':
            self.price = self.pizza.large_price

        else:
            raise ValidationError('Invalid pizza size.')

        self.subtotal = self.quantity * self.price

        super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=00.00)
