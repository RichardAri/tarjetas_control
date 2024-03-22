from django.shortcuts import render, redirect
from .forms import ProcesoForm, SubprocesoForm, TareaPruebaForm

def mi_vista_compleja(request):
    proceso_form = ProcesoForm(request.POST or None, prefix="proceso")
    subproceso_form = SubprocesoForm(request.POST or None, prefix="subproceso")
    tarea_form = TareaPruebaForm(request.POST or None, prefix="tarea")

    if 'submit_proceso' in request.POST:
        if proceso_form.is_valid():
            proceso_form.save()
            proceso_form = ProcesoForm(prefix="proceso")  # Reinicia el formulario para nuevo ingreso
    elif 'submit_subproceso' in request.POST:
        if subproceso_form.is_valid():
            subproceso_form.save()
            subproceso_form = SubprocesoForm(prefix="subproceso")  # Reinicia el formulario para nuevo ingreso
    elif 'submit_tarea' in request.POST:
        if tarea_form.is_valid():
            tarea_form.save()
            tarea_form = TareaPruebaForm(prefix="tarea")  # Reinicia el formulario para nuevo ingreso

    return render(request, 'procesos.html', {
        'proceso_form': proceso_form,
        'subproceso_form': subproceso_form,
        'tarea_form': tarea_form,
    })