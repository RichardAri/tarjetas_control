from django import forms
from .models import Proceso, Subproceso
from modelos.models import Tarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['nombre']
        labels = {
            'nombre': 'Proceso',
        }

class SubprocesoForm(forms.ModelForm):
    class Meta:
        model = Subproceso
        fields = ['proceso', 'nombre']
        labels = {
            'proceso': 'Proceso',
            'nombre': 'Subproceso',
        }

class TareaPruebaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['subproceso', 'verbo', 'objeto', 'unidad_de_medida', 'tiempo_tarea']
