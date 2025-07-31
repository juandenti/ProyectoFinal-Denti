from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def hola_mundo(request):
    return HttpResponse("Hola mundo")

def home(request):
    return render(request, 'mi_primer_app/home.html')


def crear_familiar(request, nombre):
    if nombre is not None:
        Familiar.objects.create(
            nombre=nombre, edad=30, fecha_nacimiento="1990-01-01", parentesco="Hermano")
    return render(request, 'mi_primer_app/crear-familiar.html', {"familiar":nombre})


def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'mi_primer_app/listar-familiares.html', {"familiares":familiares})
