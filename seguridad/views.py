from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from modelos.models import RecursoSeguridad

from seguridad.forms import RecursoSeguridadForm

# Create your views here.
def recursos_seguridad(request):
    # Tu lógica aquí
    return render(request, 'seguridad/recursos_seguridad.html')


#HTMX METHODS
def index(request):
    recursos = RecursoSeguridad.objects.all()
    return render(request, 'recurso_seguridad/index.html', {'recursos': recursos})

def recurso_seguridad_create(request):
    if request.method == 'POST':
        form = RecursoSeguridadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recurso-seguridad-list')
    else:
        form = RecursoSeguridadForm()
    return render(request, 'recurso_seguridad/form.html', {'form': form})

def recurso_seguridad_update(request, pk):
    recurso = get_object_or_404(RecursoSeguridad, pk=pk)
    if request.method == 'POST':
        form = RecursoSeguridadForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('recurso-seguridad-list')
    else:
        form = RecursoSeguridadForm(instance=recurso)
    return render(request, 'recurso_seguridad/form.html', {'form': form})

def recurso_seguridad_delete(request, pk):
    recurso = get_object_or_404(RecursoSeguridad, pk=pk)
    recurso.delete()
    return redirect('recurso-seguridad-list')

# END OD HTMX METHODS
