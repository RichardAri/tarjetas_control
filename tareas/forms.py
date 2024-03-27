from django import forms
from modelos.models import Tarea, RecursoSeguridad, RecursoCalidad, RecursoOperativo

class TareaForm(forms.ModelForm):
    recurso_seguridad = forms.ModelMultipleChoiceField(
        queryset=RecursoSeguridad.objects.all(),
        required=False,
        label='Recurso de Seguridad',
        widget=forms.CheckboxSelectMultiple
    )
    recurso_calidad = forms.ModelMultipleChoiceField(
        queryset=RecursoCalidad.objects.all(),
        required=False,
        label='Recurso de Calidad',
        widget=forms.CheckboxSelectMultiple
    )
    recurso_operativo = forms.ModelMultipleChoiceField(
        queryset=RecursoOperativo.objects.all(),
        required=False,
        label='Recurso Operativo',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Tarea
        fields = ['subproceso', 'verbo', 'objeto', 'unidad_de_medida', 'tiempo_tarea', 'recurso_seguridad', 'recurso_calidad', 'recurso_operativo']
