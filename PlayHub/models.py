from django.core.validators import MaxLengthValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.


plataformas = [
    ('PC', 'PC'),
    ('PS', 'PlayStation'),
    ('XB', 'Xbox'),
    ('SW', 'Switch'),
]


def validar_precio(precio):
    if precio <= 0:
        raise ValidationError("El precio tiene que ser mayor a 0.")

class Juego(models.Model):
    titulo = models.CharField(max_length=50)
    plataforma = models.CharField(choices=plataformas, max_length=2)
    precio = models.DecimalField(max_digits=4, decimal_places=2, validators=[validar_precio])
    fecha_lanzamiento = models.DateField(auto_now_add=True)

class Reseña(models.Model):
    juego_titulo = models.CharField(max_length=100)
    usuario_username = models.CharField(max_length=30)
    puntuacion = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(10)])
    comentario = models.TextField(validators=[MinLengthValidator(50)])
    fecha = models.DateField(auto_now_add=True)



