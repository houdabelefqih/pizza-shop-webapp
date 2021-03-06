from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Topping, CartItem
from django import forms


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


class ToppingsForm(ModelForm):
    class Meta:
        model = CartItem
        fields = [
            'pizza',
            'pizza_size',
            'quantity',
            'toppings',

        ]

        widgets = {
            'toppings': CheckboxSelectMultiple,
        }
