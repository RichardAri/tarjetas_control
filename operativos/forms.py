from django import forms
from operativos.models import RecursoOperativo

class OperativoForm(forms.ModelForm):
    class Meta:
        model= RecursoOperativo
        fields = (
            'nombre',
            'operativo_equipos',
            'operativo_materiales',
            'operativo_herramientas',
            'operativo_manodeobra',
            'operativo_epps',
            'operativo_generales'
        ) 
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'operativo_equipos': forms.TextInput(attrs={'class':'form-control'}),
            'operativo_materiales': forms.TextInput(attrs={'class':'form-control'}),
            'operativo_herramientas': forms.TextInput(attrs={'class':'form-control'}),
            'operativo_manodeobra': forms.TextInput(attrs={'class':'form-control'}),
            'operativo_epps': forms.TextInput(attrs={'class':'form-control'}),
            'operativo_generales': forms.TextInput(attrs={'class':'form-control'}),
        }






# class RecursoOperativo(models.Model):
#     nombre = models.CharField(max_length=100)
#     operativo_equipos = models.CharField(max_length=100)
#     operativo_materiales = models.CharField(max_length=100)
#     operativo_herramientas = models.CharField(max_length=100)
#     operativo_manodeobra = models.CharField(max_length=100)
#     operativo_epps = models.CharField(max_length=100)
#     operativo_generales = models.CharField(max_length=100)
    
#     # Otros campos relevantes para los recursos operativos