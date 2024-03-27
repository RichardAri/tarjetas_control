from django import forms
from .models import BugReport

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['tipo','description', 'image']
        labels = {
            'tipo': 'Tipo',
            'description': 'Descripción',
            'image': 'Imagen'
        }
