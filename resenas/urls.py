from django.urls import path
from .views import ResenaListView, ResenaCreateView, ResenaUpdateView, ResenaDeleteView

urlpatterns = [
    path('', ResenaListView.as_view(), name='resena_list'),
    path('crear/', ResenaCreateView.as_view(), name='resena_create'),
    path('<int:pk>/editar/', ResenaUpdateView.as_view(), name='resena_update'),
    path('<int:pk>/borrar/', ResenaDeleteView.as_view(), name='resena_delete'),
]
