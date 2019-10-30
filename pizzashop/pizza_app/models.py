from django.db import models


class PinocchioMenuItem(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    item_size = models.CharField(max_length=1, choices=SIZES, default='S')


class Pasta(PinocchioMenuItem):
    pass


class Salad(PinocchioMenuItem):
    pass


class Topping(models.Model):
    topping_name = models.CharField(max_length=255)


class Pizza(PinocchioMenuItem):
    toppings = models.ManyToManyField(Topping)


class Subs(PinocchioMenuItem):
    pass


class DinnerPlatters(PinocchioMenuItem):
    pass


class CustomerOrder(models.Model):
    pass