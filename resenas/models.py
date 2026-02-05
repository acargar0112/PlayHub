from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class Resena(models.Model):
    juego_titulo = models.CharField(max_length=100)
    usuario_username = models.CharField(max_length=30)
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comentario = models.TextField(validators=[MinLengthValidator(50)])
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return f"{self.juego_titulo} - {self.usuario_username} ({self.puntuacion})"
