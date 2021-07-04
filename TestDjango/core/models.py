from django.db import models

# Create your models here.

# Modelo para inicio de sesion
class Registro(models.Model):
    Correo= models.CharField(primary_key=True, max_length=50, verbose_name='Correo')
    Contraseña1= models.CharField(max_length=50, verbose_name='Contraseña')
    Contraseña2= models.CharField(max_length=50, verbose_name='Repita Contraseña')

    def __str__(self):
        return self.Correo


