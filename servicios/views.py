from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from servicios.forms import EquipoForm, ServicioForm
from servicios.models import Equipo, Servicio

# Create your views here.
#HTMX METHODS
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    context = {'form': EquipoForm(), 'equipos': Equipo.objects.all()}
    return render(request, 'index_equipos.html', context)

def create_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST or None)
        if form.is_valid():
            equipo = form.save()
            context = {'equipo': equipo}
            return render(request, "partials/equipo.html", context)

    return render(request, 'partials/form_equipo.html', {'form': EquipoForm()})


# servicios a partir de aqui:
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            nueva_servicio = form.save(commit=False)  # Guarda la Tarea sin enviar a la DB.
            nueva_servicio.save()  # Guarda la tarea para poder asociar los recursos muchos a muchos.
            # Asocia los recursos seleccionados con la tarea.
            nueva_servicio.equipos_necesarios.set(form.cleaned_data['equipos_necesarios'])
            nueva_servicio.save()  # Opcional, si necesitas hacer alguna otra operación después.
            return redirect('crear-servicio')
    else:
        form = ServicioForm()
    return render(request, 'Servicios/crear_servicio.html', {'form': form})

def detalle_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    # No es necesario recuperar los recursos asociados de manera explícita aquí,
    # ya que se pueden acceder directamente desde el objeto 'tarea' en el template.
    return render(request, 'Servicios/detalle_servicio.html', {'servicio': servicio})

def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'Servicios/listar_servicios.html', {'servicios': servicios})

def actualizar_cantidad_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    nueva_cantidad = int(request.POST.get('cantidad'))
    equipo.cantidad = nueva_cantidad
    equipo.save()
    return JsonResponse(equipo.cantidad, safe=False)


def eliminar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    equipo.delete()
    return JsonResponse({'success': True})
