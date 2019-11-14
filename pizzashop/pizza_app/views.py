from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, redirect
from .models import Topping, Pizza
from .forms import RegistrationForm, ToppingsForm


def index(request):
    toppings = get_list_or_404(Topping)

    pizzas = Pizza.objects.all()

    regular_pizzas = pizzas.filter(pizza_type='R')
    sicilian_pizzas = pizzas.filter(pizza_type='S')

    return render(request, 'index.html', context={'regular_pizzas': regular_pizzas,
                                                  'sicilian_pizzas': sicilian_pizzas,
                                                  'toppings': toppings,
                                                  })


def add_to_cart(request):
    if request.method == 'GET':
        toppings_form = ToppingsForm()
        return render(request, 'order.html', context={"toppings_form": toppings_form})

    elif request.method == 'POST':
        toppings_form = ToppingsForm(request.POST)

        if toppings_form.is_valid():
            toppings_form.save()
            return redirect('index')

    return render(request, 'index.html', context={"toppings_form": toppings_form})


@login_required
def display_cart(request):
    return render(request, 'cart.html')


@login_required
def display_orders(request):
    return render(request, 'orders.html')


def register(request):
    if request.method == 'GET':
        registration_form = RegistrationForm()
        return render(request, 'registration/register.html', context={"registration_form": registration_form})

    elif request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('index')

    return render(request, 'registration/register.html', context={"registration_form": registration_form})
