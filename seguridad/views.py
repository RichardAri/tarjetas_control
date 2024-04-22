from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from seguridad.models import RecursoSeguridad
from seguridad.forms import SeguridadForm
from django.contrib.auth.decorators import login_required


#HTMX METHODS
@login_required
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': SeguridadForm(), 'seguridades': RecursoSeguridad.objects.all()}
    return render(request, 'index_seguridad.html', context)

@login_required
def create_seguridad(request):
    if request.method == 'POST':
        clase = request.POST.get('clase_seguridad', '').strip()
        peligro = request.POST.get('seguridad_peligro', '').strip()
        riesgo = request.POST.get('seguridad_riesgo', '').strip()
        control = request.POST.get('seguridad_control', '').strip()
        # Verificar si todos los campos están llenos
        if clase and peligro and riesgo and control: # Si todos los campos están llenos, crear y guardar el objeto RecursoOperativo
            form = SeguridadForm(request.POST)
            seguridad = form.save()
            context = {'seguridad': seguridad }
            return render(request, 'partials/form_seguridad.html', context)  
    return render(request, 'partials/form_seguridad.html', {'form': SeguridadForm()})   


# class RecursoSeguridad(models.Model):
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     seguridad_peligro = models.CharField(max_length=100, blank=True, null=True)
#     seguridad_riesgo = models.CharField(max_length=100, blank=True, null=True)
#     seguridad_control = models.CharField(max_length=100, blank=True, null=True)
#     # Otros campos relevantes para los recursos de seguridad

