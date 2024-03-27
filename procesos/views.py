from django.shortcuts import render, redirect
from .forms import ProcesoForm, SubprocesoForm, TareaPruebaForm
from .models import Proceso, Subproceso
from modelos.models import Tarea

# ver procesos creados 
def lista_procesos(request):
    procesos = Proceso.objects.all()
    return render(request, 'procesos/lista_procesos.html', {'procesos': procesos})

# lista subprocesos creados 
def lista_subprocesos(request):
    subprocesos = Subproceso.objects.all()
    return render(request, 'subprocesos/lista_subprocesos.html', {'subprocesos': subprocesos})

# lista tareas creados 
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})



#creacion de procesos 
def mi_vista_compleja(request, proceso_id=None):
    # Inicializa el formulario de Proceso con un posible proceso existente
    proceso = Proceso.objects.filter(pk=proceso_id).first() if proceso_id else None
    
    proceso_form = ProcesoForm(request.POST or None, prefix="proceso", instance=proceso)
    subproceso_form = SubprocesoForm(request.POST or None, prefix="subproceso")
    tarea_form = TareaPruebaForm(request.POST or None, prefix="tarea")

    if 'submit_proceso' in request.POST and proceso_form.is_valid():
        proceso = proceso_form.save()
        proceso_id = proceso.id  # Actualiza el proceso_id con el id del proceso guardado
        return redirect('procesos_con_id', proceso_id=proceso_id)
    elif 'submit_subproceso' in request.POST and subproceso_form.is_valid():
        subproceso = subproceso_form.save(commit=False)
        subproceso.save()
        # Aquí asociamos el proceso actual al subproceso
        if proceso_id:
            proceso = Proceso.objects.get(pk=proceso_id)
            subproceso.proceso.add(proceso)
        return redirect('procesos_con_id', proceso_id=proceso_id)

    elif 'submit_tarea' in request.POST and tarea_form.is_valid():
        tarea = tarea_form.save(commit=False)
        tarea.save()
        # Obtener los subprocesos seleccionados desde el formulario
        subprocesos_ids = request.POST.getlist('subproceso')  # Asegúrate de que 'subproceso' es el nombre del campo en tu formulario
        for subproceso_id in subprocesos_ids:
            subproceso = Subproceso.objects.get(pk=subproceso_id)
            tarea.subprocesos.add(subproceso)
        return redirect('procesos_con_id', proceso_id=proceso_id)


    procesos = Proceso.objects.filter(pk=proceso_id) if proceso_id else Proceso.objects.none()

    return render(request, 'procesos/procesos.html', {
        'proceso_form': proceso_form,
        'subproceso_form': subproceso_form,
        'tarea_form': tarea_form,
        'procesos': procesos,
    })


