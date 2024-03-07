from django import forms
from modelos.models import Tarea, RecursoSeguridad, RecursoCalidad, RecursoOperativo

class TareaForm(forms.ModelForm):
    recurso_seguridad = forms.ModelChoiceField(
        queryset=RecursoSeguridad.objects.all(),
        required=False,
        label='Recurso de Seguridad',
        empty_label="Selecciona un Recurso de Seguridad"
    )
    recurso_calidad = forms.ModelChoiceField(
        queryset=RecursoCalidad.objects.all(),
        required=False,
        label='Recurso de Calidad',
        empty_label="Selecciona un Recurso de Calidad"
    )
    recurso_operativo = forms.ModelChoiceField(
        queryset=RecursoOperativo.objects.all(),
        required=False,
        label='Recurso Operativo',
        empty_label="Selecciona un Recurso Operativo"
    )

    class Meta:
        model = Tarea
        fields = ['verbo', 'objeto', 'orden_de_venta', 'recurso_seguridad', 'recurso_calidad', 'recurso_operativo']
