from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Pasta


def index(request):
    pastas = Pasta.objects.all()
    return render(request, 'index.html', {'pastas': pastas})


def register(request):
    form = UserCreationForm
    return render(request, "registration/register.html", {"form": form})