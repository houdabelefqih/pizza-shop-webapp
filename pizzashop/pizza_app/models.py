from django.db import models


class PinocchioMenuItem(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    item_size = models.CharField(max_length=1, choices=SIZES, null=True)

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
    toppings = models.ManyToManyField(Topping)


class Subs(PinocchioMenuItem):
    def __str__(self):
        return self.name


class DinnerPlatters(PinocchioMenuItem):
    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    pass