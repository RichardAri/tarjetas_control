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

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)  # Guarda el formulario pero no la tarea todavía
            tarea.save()  # Guarda la tarea

            # Limpia los campos ManyToMany y luego agrega los nuevos datos
            tarea.recurso_seguridad.clear()
            tarea.recurso_calidad.clear()
            tarea.recurso_operativo.clear()

            for recurso_seguridad_id in request.POST.getlist('recurso_seguridad'):
                tarea.recurso_seguridad.add(recurso_seguridad_id)
            for recurso_calidad_id in request.POST.getlist('recurso_calidad'):
                tarea.recurso_calidad.add(recurso_calidad_id)
            for recurso_operativo_id in request.POST.getlist('recurso_operativo'):
                tarea.recurso_operativo.add(recurso_operativo_id)
            
            return redirect('listar-tareas')  # Cambia 'listar-tareas' por el nombre de la URL de tu lista de tareas.
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'editar_tarea.html', {'form': form, 'tarea_id': tarea_id})


def editar_tarea_nuevo(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_tarea', tarea_id=tarea.id)  # Reemplaza 'detalle_tarea' con el nombre de tu vista de detalle
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'editar_tarea_nuevo.html', {'form': form, 'tarea': tarea})