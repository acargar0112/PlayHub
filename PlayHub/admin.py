from django.contrib import admin
from .models import Juego
# Register your models here.

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    ordering = ("-titulo",) #El orden que muestra los juegos
    list_display = ("titulo", "precio", "fecha_lanzamiento")
    search_fields = ("titulo",)
    list_filter = ("plataforma",)

    fieldsets = [
        ('Informacion de juego', {
            'fields': [
                'titulo',
                'plataforma',
            ],
        }),
        ('Detalles', {
            'fields': [
                'precio',
                'fecha_lanzamiento',
            ]
        }),
    ]