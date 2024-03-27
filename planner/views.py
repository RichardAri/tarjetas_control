from django.http import HttpResponse
from cuentas.models import UserProfile
from modelos.models import Tarea
from .models import TarjetaDiaria
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TarjetaDiariaForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone



# Create your views here.
def index_planner(request):
    return render(request, 'index_planner.html')

from django.utils import timezone
import calendar

def ver_tarjetas_diarias(request):
    usuario = request.user
    hoy = timezone.now()

    # Obtener el día y el nombre del mes actual
    dia_actual = hoy.day
    nombre_mes_actual = calendar.month_name[hoy.month]

    # Calcula el primer día del mes y su día de la semana (0 es lunes, 6 es domingo)
    primer_dia_mes = hoy.replace(day=1)
    dia_semana_primer_dia = primer_dia_mes.weekday()
    espacios_vacios = [''] * dia_semana_primer_dia

    tarjetas_diarias = TarjetaDiaria.objects.filter(
        usuario__user=usuario, 
        fecha__year=hoy.year, 
        fecha__month=hoy.month
    )

    return render(request, 'ver_tarjetas_diarias.html', {
        'tarjetas_diarias': tarjetas_diarias,
        'dia_actual': dia_actual,
        'nombre_mes_actual': nombre_mes_actual,
        'espacios_vacios': espacios_vacios,
    })


def lista_tareas(request):
    tareas = Tarea.objects.all()  # Asume que ya tienes un modelo Tarea
    return render(request, 'lista_tareas.html', {'tareas': tareas})


@login_required
def editar_tarjeta_diaria(request, tarjeta_id):  # Cambio de nombre para reflejar mejor la función
    tarjeta_diaria = get_object_or_404(TarjetaDiaria, id=tarjeta_id, usuario=request.user.userprofile)

    if request.method == 'POST':
        form = TarjetaDiariaForm(request.POST, instance=tarjeta_diaria)
        if form.is_valid():
            form.save() 
            if "HX-Request" in request.headers:
                return HttpResponse('Tarjeta Diaria actualizada exitosamente!', status=200)
            else:
                return redirect('ver_tarjetas_diarias')  # Asegúrate de reemplazar esto con una URL válida
    else:
        form = TarjetaDiariaForm(instance=tarjeta_diaria)

    if "HX-Request" in request.headers:
        return render(request, 'formulario_tarjeta_diaria.html', {'form': form, 'tarjeta_id': tarjeta_id})
    else:
        return render(request, 'ver_tarjetas_diarias.html', {'form': form})

## talves lo borre
@login_required
def crear_o_editar_tarjeta_diaria(request):
    tarjeta_id = request.GET.get('tarjeta_id', None)
    if request.method == 'POST':
        if tarjeta_id:
            tarjeta_diaria = get_object_or_404(TarjetaDiaria, id=tarjeta_id, usuario__user=request.user)  # Asegúrate de obtener la instancia correcta
            form = TarjetaDiariaForm(request.POST, instance=tarjeta_diaria)
        else:
            form = TarjetaDiariaForm(request.POST)
            
        if form.is_valid():
            tarjeta_diaria = form.save(commit=False)
            if not tarjeta_id:  # Solo asigna usuario si es una nueva tarjeta diaria
                try:
                    user_profile = UserProfile.objects.get(user=request.user)
                except UserProfile.DoesNotExist:
                    return HttpResponse('UserProfile no existe para este usuario.', status=400)
                tarjeta_diaria.usuario = user_profile
            tarjeta_diaria.save()
            form.save_m2m()  # Necesario para guardar las relaciones ManyToMany
            
            if "HX-Request" in request.headers:
                return HttpResponse('Tarjeta Diaria guardada exitosamente!', status=200)
            else:
                return redirect('ver_tarjetas_diarias')
    else:
        if tarjeta_id:
            tarjeta_diaria = get_object_or_404(TarjetaDiaria, id=tarjeta_id, usuario__user=request.user)
            form = TarjetaDiariaForm(instance=tarjeta_diaria)
        else:
            form = TarjetaDiariaForm()

    if "HX-Request" in request.headers:
        return render(request, 'formulario_tarjeta_diaria.html', {'form': form})
    else:
        return render(request, 'ver_tarjetas_diarias.html', {'form': form})
