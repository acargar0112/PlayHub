from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Juego
from .forms import JuegoForm

# Create your views here.

class Inicio(TemplateView):
    template_name = "juegos/inicio.html"


class JuegoCreateView(CreateView):
    form_class = JuegoForm # Usamos el ModelForm que hemos creado en forms.py
    template_name = "juegos/juego_form.html"
    success_url = reverse_lazy("Listado")

class JuegoListView(ListView):
    model = Juego
    template_name = "juegos/juego_list.html"
    context_object_name = "juegos"

class JuegoUpdateView(UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = "juegos/juego_form.html"
    success_url = reverse_lazy("Listado")

class JuegoDeleteView(DeleteView):
    model = Juego
    template_name = "juegos/producto_confirm_delete.html"
    success_url = reverse_lazy("Listado")
