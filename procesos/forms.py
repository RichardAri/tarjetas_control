from django import forms
from .models import Proceso, Subproceso
from modelos.models import Tarea

class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['nombre', 'descripcion']

class SubprocesoForm(forms.ModelForm):
    class Meta:
        model = Subproceso
        fields = ['nombre', 'descripcion', 'proceso']

class TareaPruebaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['verbo', 'objeto', 'orden_de_venta', 'subproceso']
