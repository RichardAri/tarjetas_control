from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from modelos.models import RecursoSeguridad
from seguridad.forms import SeguridadForm



#HTMX METHODS
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': SeguridadForm(), 'seguridades': RecursoSeguridad.objects.all()}
    return render(request, 'index_seguridad.html', context)

def create_seguridad(request):
    if request.method == 'POST':
        form = SeguridadForm(request.POST or None)
        if form.is_valid():
            seguridad = form.save()
            context = {'seguridad': seguridad}
            return render(request, "partials/seguridad.html", context)

    return render(request, 'partials/form_seguridad.html', {'form': SeguridadForm()})

# class RecursoSeguridad(models.Model):
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     seguridad_peligro = models.CharField(max_length=100, blank=True, null=True)
#     seguridad_riesgo = models.CharField(max_length=100, blank=True, null=True)
#     seguridad_control = models.CharField(max_length=100, blank=True, null=True)
#     # Otros campos relevantes para los recursos de seguridad

