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
        form = CalidadForm(request.POST or None)
        if form.is_valid():
            recurso = form.save()
            context = {'contact': recurso}
            return render(request, 'partials/recurso.html', context)

    return render(request, 'partials/form.html', {'form': CalidadForm })

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