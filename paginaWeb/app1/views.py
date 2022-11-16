from django.shortcuts import render
from django.http import HttpResponse
from .models import cine, pelicula, cliente
from .forms import cineForm, peliculaForm, clienteForm

# Create your views here.
def mostrar_index(request):
    return render(request, 'index.html')


def buscar_pelicula(request):

    consulta_pelicula = pelicula(nombre=['nombre'], duracion=['duracion'])
    
    return render(request, 'consulta_pelicula.html' ,{'pelicula':[consulta_pelicula]})

def buscar_cine(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        CINE =cine.objects.filter(cine__icontains=cine)
        return render(request, 'consulta_cine.html', {'CINE': CINE})

    else:
        respuesta = 'no hay datos ingresados...'
        return render(request, 'consulta_cine.html', {'respuesta': respuesta})