from django import forms
from modelos.models import RecursoSeguridad

class SeguridadForm(forms.ModelForm):
    class Meta:
        model = RecursoSeguridad
        fields = ('clase_seguridad', 'seguridad_peligro', 'seguridad_riesgo', 'seguridad_control')
        widgets = {
            'clase_seguridad': forms.TextInput(attrs={'class':'form-control'}),
            'seguridad_peligro': forms.TextInput(attrs={'class':'form-control'}),
            'seguridad_riesgo': forms.TextInput(attrs={'class':'form-control'}),
            'seguridad_control': forms.TextInput(attrs={'class':'form-control'}),
        }
