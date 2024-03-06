from django.http import HttpResponse
from django.shortcuts import render
from modelos.models import RecursoOperativo
from operativos.forms import OperativoForm

# Create your views here.
def recursos_operativos(request):
    # Tu lógica aquí
    return render(request, 'operativos/recursos_operativos.html')

def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': OperativoForm(), 'operativos': RecursoOperativo.objects.all()}
    return render(request, 'operativos_index.html', context)

def create_operativo(request):
    if request.method == 'POST':
        form = OperativoForm(request.POST or None)
        if form.is_valid():
            operativo = form.save()
            context = {'operativo': operativo }
            return render(request, 'partials/operativos.html', context)


    return render(request, 'partials/form_seguridad.html', {'form': OperativoForm()})   