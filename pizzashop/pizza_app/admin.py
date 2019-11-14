from django.contrib import admin

# Register your models here.
from pizza_app.models import Topping, Pizza, Cart, CartItem

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Cart)
admin.site.register(CartItem)
