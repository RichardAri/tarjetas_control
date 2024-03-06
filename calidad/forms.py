from django import forms
from modelos.models import RecursoCalidad


class CalidadForm(forms.ModelForm):
    class Meta:
        model = RecursoCalidad
        fields = (
            'nombre', 'calidad_peligro', 'calidad_riesgo', 'calidad_causas', 'calidad_control',
        )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'calidad_peligro': forms.TextInput(attrs={'class': 'form-control'}),
            'calidad_riesgo': forms.TextInput(attrs={'class': 'form-control'}),
            'calidad_causas': forms.TextInput(attrs={'class': 'form-control'}),
            'calidad_control': forms.TextInput(attrs={'class': 'form-control'})
        }
