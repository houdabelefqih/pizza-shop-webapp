from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', )


def register(request):
    form = UserCreationForm
    return render(request, "registration/register.html", {"form": form})