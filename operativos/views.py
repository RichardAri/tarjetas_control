from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from operativos.models import RecursoOperativo
from operativos.forms import OperativoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': OperativoForm(), 'operativos': RecursoOperativo.objects.all()}
    return render(request, 'operativos_index.html', context)

@login_required
def create_operativo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        equipos = request.POST.get('operativo_equipos', '').strip()
        materiales = request.POST.get('operativo_materiales', '').strip()
        herramientas = request.POST.get('operativo_herramientas', '').strip()
        manoDeObra = request.POST.get('operativo_manodeobra', '').strip()
        epps = request.POST.get('operativo_epps', '').strip()
        generales = request.POST.get('operativo_generales', '').strip()

        # Verificar si todos los campos están llenos
        if nombre and equipos and materiales and herramientas and manoDeObra and epps and generales:
            # Si todos los campos están llenos, crear y guardar el objeto RecursoOperativo
            form = OperativoForm(request.POST)
            operativo = form.save()
            context = {'operativo': operativo }
            #return render(request, 'partials/operativos.html', context)
            return render(request, 'partials/form_operativos.html', {'form': OperativoForm()})  
    return render(request, 'partials/form_operativos.html', {'form': OperativoForm()})   