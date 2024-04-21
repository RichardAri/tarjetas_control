from django.http import HttpResponse
from django.shortcuts import render
from modelos.models import RecursoOperativo
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
        form = OperativoForm(request.POST or None)
        if form.is_valid():
            operativo = form.save()
            context = {'operativo': operativo }
            return render(request, 'partials/operativos.html', context)


    return render(request, 'partials/form_operativos.html', {'form': OperativoForm()})   