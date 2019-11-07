from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_list_or_404
from .models import Pasta, Salad, DinnerPlatters, Topping, Subs


def index(request):
    salads = get_list_or_404(Salad)
    pastas = get_list_or_404(Pasta)
    dinner_platters = get_list_or_404(DinnerPlatters)
    toppings = get_list_or_404(Topping)
    subs = get_list_or_404(Subs)
    return render(request, 'index.html', {'pastas': pastas,
                                          'salads': salads,
                                          'dinner_platters': dinner_platters,
                                          'toppings': toppings,
                                          'subs': subs, })


def register(request):
    form = UserCreationForm
    return render(request, "registration/register.html", {"form": form})
