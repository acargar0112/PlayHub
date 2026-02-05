from os import name

from django.urls import path
from .views import (
    Inicio,
    JuegoCreateView,
    JuegoListView,
    JuegoUpdateView,
    JuegoDeleteView,
)

urlpatterns = [
    path('', Inicio.as_view(), name='Inicio'),
    path('juego/', JuegoCreateView.as_view(), name='Formulario'),
    path('juego/listar', JuegoListView.as_view(), name="Listado"),
    path('juego/<int:pk>/editar/', JuegoUpdateView.as_view(), name="Update"),
    path('juego/<int:pk>/borrar/', JuegoDeleteView.as_view(), name="Delete"),
]
