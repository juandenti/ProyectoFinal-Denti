from django.contrib import admin
from .models import Perfume, Marca, Vela, Perfumista

# Register your models here.

register_models = [Perfume,Marca,Vela,Perfumista]

admin.site.register(register_models)