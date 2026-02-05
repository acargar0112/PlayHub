from django.contrib import admin
from .models import Resena


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ("juego_titulo", "usuario_username", "puntuacion", "fecha")
    search_fields = ("juego_titulo", "usuario_username")
    list_filter = ("puntuacion",)
