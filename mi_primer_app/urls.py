
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cargar-perfume/', views.cargar_perfume, name='cargar-perfume'),
    path('cargar-marca/', views.cargar_marca, name='cargar-marca'),
    path('cargar-vela/', views.cargar_vela, name='cargar-vela'),
    path('buscar-perfumes/', views.buscar_perfumes, name="buscar-perfumes"),

]   

