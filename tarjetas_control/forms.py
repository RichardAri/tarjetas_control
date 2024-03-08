from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from modelos.models import TarjetaDeControl, Tarea

class TarjetaDeControlForm(forms.ModelForm):
    tareas = forms.ModelMultipleChoiceField(
        queryset=Tarea.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tareas'
    )

    class Meta:
        model = TarjetaDeControl
        fields = ['titulo', 'valorizacion', 'tareas']
