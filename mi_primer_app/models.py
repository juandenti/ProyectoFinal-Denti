from django.db import models

# Create your models here.

    
class Perfume(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_de_aroma = models.TextField()
    duracion = models.TextField()
    concentracion = models.TextField()
    empresa = models.TextField()

    def __str__(self):
        return self.nombre
    


class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fundada = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    


class Vela(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_de_aroma = models.TextField()
    empresa = models.TextField()

    def __str__(self):
        return self.nombre
    
class Perfumista(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.CharField(max_length=20)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.edad} {self.nombre}'