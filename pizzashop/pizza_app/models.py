from django.core.validators import MaxLengthValidator
from django.db import models
from rest_framework.compat import MaxValueValidator


class PinocchioMenuItem(models.Model):

    name = models.CharField(max_length=255)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        abstract = True


class Pasta(PinocchioMenuItem):

    def __str__(self):
        return self.name


class Salad(PinocchioMenuItem):
    def __str__(self):
        return self.name


class Topping(models.Model):
    topping_name = models.CharField(max_length=255)


class Pizza(PinocchioMenuItem):
    PIZZA_TYPES = (
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )
    max_toppings = models.PositiveSmallIntegerField(default= 0, validators=[MaxValueValidator(9), MaxValueValidator(9)])
    toppings = models.ManyToManyField(Topping)
    pizza_type = models.CharField(max_length=1, choices=PIZZA_TYPES, null=True)


class Subs(PinocchioMenuItem):
    def __str__(self):
        return self.name


class DinnerPlatters(PinocchioMenuItem):
    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    pass