from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Perfume, Marca, Vela, Perfumista
from .forms import PerfumeForm, MarcaForm, VelaForm, PerfumistaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'mi_primer_app/home.html')
        

@login_required       
def cargar_perfume(request):
    if request.method == 'POST':
        form = PerfumeForm(request.POST)
        if form.is_valid():
            perfume = Perfume(
                nombre=form.cleaned_data['nombre'],
                tipo_de_aroma=form.cleaned_data['tipo_de_aroma'],
                duracion=form.cleaned_data['duracion'],
                concentracion=form.cleaned_data['concentracion'],
                empresa=form.cleaned_data['empresa'],
            )
            perfume.save()
            return redirect("home")
    form = PerfumeForm()
    return render(request, 'mi_primer_app/cargar-perfume.html', {"form":form})   


@login_required  
def cargar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            marca = Marca(
                nombre=form.cleaned_data['nombre'],
                fecha_fundada=form.cleaned_data['fecha_fundada'],
                activo=form.cleaned_data['activo'],
            )
            marca.save()
            return redirect("home") 
    form = MarcaForm()
    return render(request, 'mi_primer_app/cargar-marca.html', {"form":form})       
        
@login_required  
def cargar_vela(request):
    if request.method == 'POST':
        form = VelaForm(request.POST)
        if form.is_valid():
            vela = Vela(
                nombre=form.cleaned_data['nombre'],
                tipo_de_aroma=form.cleaned_data['tipo_de_aroma'],
                empresa=form.cleaned_data['empresa'],
            )
            vela.save()
            return redirect("home")  
    form = VelaForm()
    return render(request, 'mi_primer_app/cargar-vela.html', {"form":form})     

        
def buscar_perfumes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre' , '')
        perfumes = Perfume.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/buscar-perfumes.html', {"perfumes":perfumes, "nombre":nombre})  
    
def about(request):
    return render(request, 'mi_primer_app/about.html')


# Vistas basadas en clases para Perfumista

class PerfumistaListView(ListView):
    model = Perfumista
    template_name = 'mi_primer_app/listar-perfumistas.html'
    context_object_name = "perfumistas"

class PerfumistaCreateView(LoginRequiredMixin, CreateView):
    model = Perfumista
    form_class = PerfumistaForm
    template_name = 'mi_primer_app/crear-perfumistas.html'
    success_url = reverse_lazy('listar-perfumistas')

class PerfumistaUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfumista
    form_class = PerfumistaForm
    template_name = 'mi_primer_app/crear-perfumistas.html'
    success_url = reverse_lazy('listar-perfumistas')

class PerfumistaDetailView(LoginRequiredMixin, DetailView):
    model = Perfumista
    template_name = 'mi_primer_app/detalle-perfumistas.html'
    context_object_name = "perfumista"

class PerfumistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Perfumista
    template_name = 'mi_primer_app/eliminar-perfumistas.html'
    success_url = reverse_lazy('listar-perfumistas')