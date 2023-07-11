from django import forms
from .models import contacto, producto
from django.contrib.auth.forms import UserCreationForm


class contactoform(forms.ModelForm):

    class Meta:
        model = contacto
        fields = '__all__'


class productoform(forms.ModelForm):

    class Meta:
        model = producto
        fields = '__all__'

class CustomUserForm(UserCreationForm):
    pass