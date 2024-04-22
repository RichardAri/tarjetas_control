from django.shortcuts import render
from django.http import HttpResponse
from calidad.forms import CalidadForm
from calidad.models import RecursoCalidad
from django.contrib.auth.decorators import login_required

@login_required
def recursos_calidad(request):
    # Tu lógica aquí
    return render(request, 'calidad/recursos_calidad.html')

@login_required
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': CalidadForm(), 'recursos': RecursoCalidad.objects.all()}
    return render(request, 'index.html', context)

@login_required
def create_recurso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        peligro = request.POST.get('calidad_peligro', '').strip()
        riesgo = request.POST.get('calidad_riesgo', '').strip()
        causas = request.POST.get('calidad_causas', '').strip()
        control = request.POST.get('calidad_control', '').strip()

        # Verificar si todos los campos están llenos
        if nombre and peligro and riesgo and causas and control: # Si todos los campos están llenos, crear y guardar el objeto RecursoOperativo
            form = CalidadForm(request.POST)
            recurso = form.save()
            context = {'contact': recurso }
            return render(request, 'partials/recurso.html', context)
    return render(request, 'partials/form.html', {'form': CalidadForm })

# !agrega normal los datos pero la pagina /calidad no se recarga 
# !por lo que el usuario debe de actualizar la pagina 
# !para ver los datos
