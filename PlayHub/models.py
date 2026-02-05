from django.core.validators import MaxLengthValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.


def validar_precio(precio):
    if precio <= 0:
        raise ValidationError("El precio tiene que ser mayor a 0.")

class Juego(models.Model): # Añadir verbose_name a todos.
    plataformas = [
        ('PC', 'PC'),
        ('PS', 'PlayStation'),
        ('XB', 'Xbox'),
        ('SW', 'Switch'),
    ]
    """
    OTRA FORMA DE HACER EL CHOICE, AUNQUE EL OTRO TAMBIEN DEBERIA DE ESTAR DENTRO DE LA CLASE.
        
    plataformas = {
        'PC': 'PC',
        'PS': 'PlayStation',
        'XB': 'XB',
        'SW': 'Switch',
    }
    """
    titulo = models.CharField(max_length=50, verbose_name="Titulo")
    plataforma = models.CharField(choices=plataformas, max_length=2, verbose_name="Plataforma")
    precio = models.DecimalField(max_digits=4, decimal_places=2, validators=[validar_precio], verbose_name="Precio")
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de la lanzamiento") # No utilizar auto, ya que esta fecha se pondrá al crear.

"""  
class Meta:
    verbose_name = "Juego"
    verbose_name_plural = "Juegos"
    ordering = ["-fecha_lanzamiento"] #Orden en el que me da los objetos por defecto

def __str__(self):
    return f"{self.titulo} ({self.plataforma})"

def clean(self):
    if self.precio is not None and self.precio <= 0.0:
        raise ValidationError({precio}: "Precio tiene que ser mayor a 0.")
"""




