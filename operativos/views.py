from django.http import HttpResponse
from django.shortcuts import render
from modelos.models import RecursoOperativo
from operativos.forms import OperativoForm

# Create your views here.
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


    return render(request, 'partials/form_operativos.html', {'form': OperativoForm()})   