from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProcesoForm, SubprocesoForm, TareaPruebaForm
from .models import Proceso, Subproceso
from modelos.models import Tarea
from .forms import ProcesosForm, ProcesoEditForm

# ver procesos creados 
def lista_procesos(request):
    procesos = Proceso.objects.all()
    return render(request, 'procesos/lista_procesos.html', {'procesos': procesos})

def ver_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    subprocesos = proceso.subprocesos.all()  # Ajusta esto según tu modelo

    return render(request, 'procesos/ver_proceso.html', {
        'proceso': proceso,
        'subprocesos': subprocesos
    })

def crear_proceso(request):
    if request.method == 'POST':
        form = ProcesosForm(request.POST)
        if form.is_valid():
            proceso = form.save(commit=False)
            proceso.save()  # Guarda el Proceso para obtener un ID.

            # Ahora establece explícitamente las relaciones ManyToMany.
            # Asegúrate de que 'subprocesos' es el nombre correcto del campo en tu formulario.
            proceso.subprocesos.set(form.cleaned_data['subprocesos'])

            return redirect('lista_procesos')
    else:
        form = ProcesosForm()

    return render(request, 'procesos/crear_proceso.html', {'form': form})

def eliminar_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    if request.method == 'POST':
        proceso.delete()
        return HttpResponse('')  # Respuesta vacía para HTMX
    else:
        return redirect('lista_procesos') 
    
def editar_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    if request.method == 'POST':
        form = ProcesoEditForm(request.POST, instance=proceso)
        if form.is_valid():
            proceso = form.save()
            proceso.subprocesos.set(form.cleaned_data['subprocesos'])
            proceso.tareas.set(form.cleaned_data['tareas'])
            return redirect('lista_procesos')
    else:
        form = ProcesoEditForm(instance=proceso)
        
    return render(request, 'procesos/editar_proceso.html', {'form': form})



# acaba procesos 



# lista subprocesos creados 
def lista_subprocesos(request):
    subprocesos = Subproceso.objects.all()
    return render(request, 'subprocesos/lista_subprocesos.html', {'subprocesos': subprocesos})

def ver_subproceso(request, subproceso_id):
    subproceso = get_object_or_404(Subproceso, pk=subproceso_id)
    tareas = subproceso.tareas.all()  # Esto recupera todas las tareas relacionadas

    return render(request, 'subprocesos/ver_subproceso.html', {
        'subproceso': subproceso,
        'tareas': tareas
    })




# lista tareas creados 
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})


# creacion de procesos con subprocesos

#creacion de procesos 
def mi_vista_compleja(request, proceso_id=None, subproceso_id=None):
    # Inicializa el formulario de Proceso con un posible proceso existente
    proceso = Proceso.objects.filter(pk=proceso_id).first() if proceso_id else None
    
    proceso_form = ProcesoForm(request.POST or None, prefix="proceso", instance=proceso)
    subproceso_form = SubprocesoForm(request.POST or None, prefix="subproceso")
    tarea_form = TareaPruebaForm(request.POST or None, prefix="tarea")
    

    if 'submit_proceso' in request.POST and proceso_form.is_valid():
        proceso = proceso_form.save()
        proceso_id = proceso.id  # Actualiza el proceso_id con el id del proceso guardado
        
        if subproceso_id is not None:
            return redirect('procesos_con_id', proceso_id=proceso_id, subproceso_id=subproceso_id)
        else:
            return redirect('procesos_con_id', proceso_id=proceso_id)

    elif 'submit_subproceso' in request.POST and subproceso_form.is_valid():
        subproceso = subproceso_form.save(commit=False)
        subproceso.save()
        subproceso_id = subproceso.id
        # Aquí asociamos el proceso actual al subproceso
        if proceso_id:
            proceso = Proceso.objects.get(pk=proceso_id)
            subproceso.proceso.add(proceso)
        return redirect('procesos_con_id', proceso_id=proceso_id, subproceso_id=subproceso_id)

    elif 'submit_tarea' in request.POST and tarea_form.is_valid():
        tarea = tarea_form.save(commit=False)
        tarea.save()
        # Suponiendo que has capturado un subproceso_id de alguna manera
        if subproceso_id:
            subproceso = Subproceso.objects.get(pk=subproceso_id)
            tarea.subproceso.add(subproceso)
        return redirect('procesos_con_id', proceso_id=proceso_id, subproceso_id=subproceso_id)

    procesos = Proceso.objects.filter(pk=proceso_id).prefetch_related('subprocesos__tareas') if proceso_id else Proceso.objects.none()


    return render(request, 'procesos/procesos.html', {
        'proceso_form': proceso_form,
        'subproceso_form': subproceso_form,
        'tarea_form': tarea_form,
        'procesos': procesos,
    })

def editar_proceso(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form = ProcesoForm(request.POST, instance=proceso)
        if form.is_valid():
            form.save()
            # Puedes agregar un mensaje de éxito aquí si lo deseas
            return redirect('ruta_de_redireccion')  # Especifica la URL a la que deseas redirigir después de guardar los cambios
    else:
        form = ProcesoForm(instance=proceso)
    
    return render(request, 'procesos/editar_proceso.html', {'form': form, 'proceso': proceso})
