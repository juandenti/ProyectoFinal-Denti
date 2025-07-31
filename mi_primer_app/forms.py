from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label= 'Descripción')
    duracion_semanas = forms.IntegerField(label= 'Duración (semanas)')
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget, label='fecha de inicio')
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget, label='fecha de fin')
    activo = forms.BooleanField(required=False, initial=True, label= 'Activo')

    def __str__(self):
        return self.nombre
    
class PerfumeForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Perfume')
    tipo_de_aroma = forms.CharField(widget=forms.Textarea, label= 'Tipo de aroma')
    duracion = forms.IntegerField(label= 'Duración (horas)')
    concentracion = forms.CharField(max_length=100, label='EDT/EDP')
    empresa = forms.CharField(max_length=100, label='Nombre de la Marca Creadora')

class MarcaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre de la marca')
    fecha_fundada = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de fundación')
    activo = forms.BooleanField(required=False, initial=True, label= 'Activo')

class VelaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre de la vela aromática')
    tipo_de_aroma = forms.CharField(widget=forms.Textarea, label= 'Tipo de aroma')
    empresa = forms.CharField(max_length=100, label='Nombre de la Marca Creadora')