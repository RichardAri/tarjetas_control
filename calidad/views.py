from django.shortcuts import render
from django.http import HttpResponse
from calidad.forms import CalidadForm
from modelos.models import RecursoCalidad

def recursos_calidad(request):
    # Tu lógica aquí
    return render(request, 'calidad/recursos_calidad.html')

def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': CalidadForm(), 'recursos': RecursoCalidad.objects.all()}
    return render(request, 'index.html', context)

def create_recurso(request):
    if request.method == 'POST':
        form = CalidadForm(request.POST or None)
        if form.is_valid():
            recurso = form.save()
            context = {'contact': recurso}
            return render(request, 'partials/recurso.html', context)

    return render(request, 'partials/form.html', {'form': CalidadForm })