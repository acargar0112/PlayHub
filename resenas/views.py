from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resena
from .forms import ResenaForm


class ResenaListView(LoginRequiredMixin, ListView):
    model = Resena
    template_name = "resenas/resena_list.html"
    context_object_name = "resenas"


class ResenaCreateView(LoginRequiredMixin, CreateView):
    form_class = ResenaForm
    template_name = "resenas/resena_form.html"
    success_url = reverse_lazy("resena_list")

    def form_valid(self, form):
        form.instance.usuario_username = self.request.user.username
        return super().form_valid(form)


class ResenaUpdateView(LoginRequiredMixin, UpdateView):
    model = Resena
    form_class = ResenaForm
    template_name = "resenas/resena_form.html"
    success_url = reverse_lazy("resena_list")

    def form_valid(self, form):
        form.instance.usuario_username = self.get_object().usuario_username
        return super().form_valid(form)


class ResenaDeleteView(LoginRequiredMixin, DeleteView):
    model = Resena
    template_name = "resenas/resena_confirm_delete.html"
    success_url = reverse_lazy("resena_list")
