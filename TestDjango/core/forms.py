from django import forms
from django.forms import ModelForm
from .models import Registro

class RegistroForm(ModelForm):
    class Meta: 
        model=Registro
        fields=['Correo','Contraseña1','Contraseña2']
