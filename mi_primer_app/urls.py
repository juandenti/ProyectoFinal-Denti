
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cargar-perfume/', views.cargar_perfume, name='cargar-perfume'),
    path('cargar-marca/', views.cargar_marca, name='cargar-marca'),
    path('cargar-vela/', views.cargar_vela, name='cargar-vela'),
    path('buscar-perfumes/', views.buscar_perfumes, name="buscar-perfumes"),
    path('about/', views.about, name="about"),

    #Vistas basadas en clases

    path('crear-perfumistas/', views.PerfumistaCreateView.as_view(), name="crear-perfumistas"),
    path('listar-perfumistas/', views.PerfumistaListView.as_view(), name="listar-perfumistas"),

    path('detalle-perfumistas/<int:pk>/', views.PerfumistaDetailView.as_view(), name="detalle-perfumistas"),
    path('editar/<int:pk>/', views.PerfumistaUpdateView.as_view(), name="editar-perfumistas"),
    path('eliminar/<int:pk>/', views.PerfumistaDeleteView.as_view(), name="eliminar-perfumistas"),

]   
