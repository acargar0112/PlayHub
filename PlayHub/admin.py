from django.contrib import admin
from .models import Juego
# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "precio", "fecha_lanzamiento"]
    search_fields = ["titulo"]
    list_filter = ["plataforma"]

admin.site.register(Juego, JuegoAdmin)
