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
    if request.user.userprofile.rol == 'jefe':
        tarjetas = TarjetaDeControl.objects.all().prefetch_related('tareas')
    else:
        tarjetas = TarjetaDeControl.objects.filter(usuario=request.user).prefetch_related('tareas')
    return render(request, 'listar_tarjetas_control.html', {'tarjetas': tarjetas})

@login_required
def crear_editar_tarjeta_control(request, tarjeta_id=None):
    es_jefe = request.user.userprofile.rol == 'jefe'
    tarjeta = None
    if tarjeta_id:
        if es_jefe:
            tarjeta = get_object_or_404(TarjetaDeControl, id=tarjeta_id)
        else:
            tarjeta = get_object_or_404(TarjetaDeControl, id=tarjeta_id, usuario=request.user)
    else:
        # Esto indica que estamos creando una nueva tarjeta, no editando una existente.
        tarjeta = TarjetaDeControl(usuario=request.user)  # Asignar aquí el usuario

    if request.method == 'POST':
        form = TarjetaDeControlForm(request.POST, instance=tarjeta)
        if form.is_valid():
            nueva_tarjeta = form.save(commit=False)
            # Si tarjeta_id no está definido, significa que es una nueva tarjeta y ya hemos asignado el usuario.
            if not tarjeta_id:
                nueva_tarjeta.usuario = request.user  # Esto es seguro porque es una nueva tarjeta.
            nueva_tarjeta.save()
            form.save_m2m()
            return redirect('listar_tarjetas_control')
    else:
        form = TarjetaDeControlForm(instance=tarjeta)

    return render(request, 'crear_editar_tarjeta_control.html', {'form': form})

@login_required
def detalle_tarjeta_control(request, tarjeta_id):
    # Comprobar si el usuario es jefe
    es_jefe = request.user.userprofile.rol == 'jefe'
    if es_jefe:
        tarjeta = get_object_or_404(TarjetaDeControl, id=tarjeta_id)
    else:
        tarjeta = get_object_or_404(TarjetaDeControl, id=tarjeta_id, usuario=request.user)
    return render(request, 'detalle_tarjeta_control.html', {'tarjeta': tarjeta})

