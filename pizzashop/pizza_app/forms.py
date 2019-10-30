from django.forms import ModelForm
from .models import RegistrationData


class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationData
        fields = ['first_name', 'last_name', 'email', 'phone_number']