from django import forms
    
class PerfumeForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Perfume')
    tipo_de_aroma = forms.CharField(widget=forms.Textarea, label= 'Tipo de aroma')
    duracion = forms.IntegerField(label= 'Duración (horas)')
    concentracion = forms.CharField(max_length=100, label='EDT/EDP')
    empresa = forms.CharField(max_length=100, label='Nombre de la Marca Creadora')

    def __str__(self):
        return self.nombre

class MarcaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre de la marca')
    fecha_fundada = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de fundación')
    activo = forms.BooleanField(required=False, initial=True, label= 'Activo')

    def __str__(self):
        return self.nombre

class VelaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre de la vela aromática')
    tipo_de_aroma = forms.CharField(widget=forms.Textarea, label= 'Tipo de aroma')
    empresa = forms.CharField(max_length=100, label='Nombre de la Marca Creadora')

    def __str__(self):
        return self.nombre