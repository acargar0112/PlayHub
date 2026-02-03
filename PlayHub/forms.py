from django import forms
from .models import Juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ["titulo", "plataforma", "precio","fecha_lanzamiento"]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cyberpunk 2077',
            }),"""
            'plataforma': forms.TextInput(attrs={
                'class': 'form-control',
            }),"""
            'precio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '99.99',
                'step': '0.01',
            }),
            'fecha_lanzamiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            })
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0")
        return precio