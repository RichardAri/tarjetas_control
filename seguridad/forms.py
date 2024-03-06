from django import forms
from modelos.models import RecursoSeguridad

class RecursoSeguridadForm(forms.ModelForm):
    class Meta:
        model = RecursoSeguridad
        fields = ['nombre', 'seguridad_peligro', 'seguridad_riesgo', 'seguridad_control']
