from django import forms
from modelos.models import Tarea
from .models import TarjetaDiaria

class TarjetaDiariaForm(forms.ModelForm):
    tareas = forms.ModelMultipleChoiceField(
        queryset=Tarea.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tareas'
    )

    class Meta:
        model = TarjetaDiaria
        fields = ['fecha', 'tareas']  # Asume que TarjetaDiaria tiene al menos estos dos campos: 'fecha' y 'tareas'
