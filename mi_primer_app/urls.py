
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('hola-mundo/', views.hola_mundo, name='hola_mundo'),
    # path('crear-curso/', views.crear_curso , name='crear-curso'),
    # path('listar-cursos/', views.listar_cursos, name="listar-cursos"),
    # path('cursos/buscar/', views.buscar_cursos, name="buscar-cursos"),

    path('cargar-perfume/', views.cargar_perfume, name='cargar-perfume'),
    path('cargar-marca/', views.cargar_marca, name='cargar-marca'),
    path('cargar-vela/', views.cargar_vela, name='cargar-vela'),
    path('buscar-perfumes/', views.buscar_perfumes, name="buscar-perfumes"),

]   

