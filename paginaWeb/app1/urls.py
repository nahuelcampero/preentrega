from django import path
from app1.views import mostrar_index, buscar_CINE, buscar_pelicula
from .forms import cineForm, peliculaForm, clienteForm


urlpatterns = [
    path('mostrar_index/', mostrar_index),
    path('buscar_CINE/', buscar_CINE, name='buscar buscar_CINE'),
    path('buscar_pelicula/', buscar_pelicula, name='buscar pelicula'),
    path('cineForm/', cineForm),
    path('peliculaForm/', peliculaForm),
    path('clienteForm/', clienteForm),
]