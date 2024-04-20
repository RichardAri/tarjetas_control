from django import forms
from .models import Equipo, Servicio

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('nombre', 'descripcion', 'cantidad')  # Campos del modelo Equipo que deseas incluir en el formulario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),  # Establecer valor predeterminado a 0
        }

class ServicioForm(forms.ModelForm):
    equipos_necesarios = forms.ModelMultipleChoiceField(
        queryset=Equipo.objects.all(),
        required=False,
        label='Equipos para tu servicio',
        widget=forms.CheckboxSelectMultiple
    )
    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'supervisor', 'fecha', 'costo', 'estado', 'equipos_necesarios']
