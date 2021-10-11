from django import forms
from django.db import models
from django.forms import fields
from .models import Cliente, Profesional
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
       #fields = ["rut_cliente","nombre","correo","empresa","telefono"]
        fields = '__all__' 

class ProfesionalForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
     
     class Meta:
         model = User
         fields = ['username', "first_name", "last_name", "email", "password1", "password2"]