from django import forms
from PlayHub.models import Juego
from .models import Resena


class ResenaForm(forms.ModelForm):
    juego_titulo = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Resena
        fields = ["juego_titulo", "puntuacion", "comentario"]
        widgets = {
            'puntuacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        juegos = Juego.objects.values_list('titulo', 'titulo')
        self.fields['juego_titulo'].choices = [('', '--- Selecciona un juego ---')] + list(juegos)

    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario', '')
        if comentario and len(comentario.strip()) < 50:
            raise forms.ValidationError('El comentario debe tener al menos 50 caracteres.')
        return comentario
