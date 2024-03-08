from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from modelos.models import Tarea
from tareas.forms import TareaForm

# Create your views here.
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    return HttpResponse("¡Bienvenido tareas!")

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False)  # Guarda la Tarea sin enviar a la DB.
            nueva_tarea.save()  # Guarda la tarea para poder asociar los recursos muchos a muchos.
            # Asocia los recursos seleccionados con la tarea.
            nueva_tarea.recurso_seguridad.set(form.cleaned_data['recurso_seguridad'])
            nueva_tarea.recurso_calidad.set(form.cleaned_data['recurso_calidad'])
            nueva_tarea.recurso_operativo.set(form.cleaned_data['recurso_operativo'])
            nueva_tarea.save()  # Opcional, si necesitas hacer alguna otra operación después.
            return redirect('crear-tarea')
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    # No es necesario recuperar los recursos asociados de manera explícita aquí,
    # ya que se pueden acceder directamente desde el objeto 'tarea' en el template.
    return render(request, 'detalle_tarea.html', {'tarea': tarea})

def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'listar_tareas.html', {'tareas': tareas})