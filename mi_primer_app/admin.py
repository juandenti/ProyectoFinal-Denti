from django.contrib import admin
from .models import Perfume, Marca, Vela

# Register your models here.

register_models = [Perfume,Marca,Vela]

admin.site.register(register_models)