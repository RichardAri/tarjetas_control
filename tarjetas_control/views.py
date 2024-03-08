from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from modelos.models import TarjetaDeControl
from tarjetas_control.forms import TarjetaDeControlForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    return HttpResponse("¡Bienvenido tarjetas control!")

@login_required
def listar_tarjetas_control(request):
    tarjetas = TarjetaDeControl.objects.filter(usuario=request.user).prefetch_related('tareas')
    return render(request, 'listar_tarjetas_control.html', {'tarjetas': tarjetas})

@login_required
def crear_editar_tarjeta_control(request, tarjeta_id=None):
    tarjeta = None
    if tarjeta_id:
        tarjeta = get_object_or_404(TarjetaDeControl, id=tarjeta_id, usuario=request.user)
    if request.method == 'POST':
        form = TarjetaDeControlForm(request.POST, instance=tarjeta)
        if form.is_valid():
            nueva_tarjeta = form.save(commit=False)
            nueva_tarjeta.usuario = request.user  # Asigna el usuario a la tarjeta
            nueva_tarjeta.save()
            form.save_m2m()
            return redirect('listar_tarjetas_control')
    else:
        form = TarjetaDeControlForm(instance=tarjeta)

    return render(request, 'crear_editar_tarjeta_control.html', {'form': form})

@login_required
def detalle_tarjeta_control(request, tarjeta_id):
    tarjeta = get_object_or_404(TarjetaDeControl, id=tarjeta_id, usuario=request.user)
    return render(request, 'detalle_tarjeta_control.html', {'tarjeta': tarjeta})

