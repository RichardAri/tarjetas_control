from django.http import HttpResponse
from django.shortcuts import render
from .models import TarjetaDiaria
# Create your views here.
def index_planner(request):
    return render(request, 'index_planner.html')

def ver_tarjetas_diarias(request):
    # Obtener el usuario autenticado
    usuario = request.user

    # Filtrar las tarjetas diarias por el usuario autenticado
    tarjetas_diarias = TarjetaDiaria.objects.filter(usuario__user=usuario)

    # Pasar los datos a la plantilla
    return render(request, 'ver_tarjetas_diarias.html', {'tarjetas_diarias': tarjetas_diarias})
