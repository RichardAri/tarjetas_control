from django.http import HttpResponse
from django.shortcuts import redirect, render

from tareas.forms import TareaForm

# Create your views here.
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    return HttpResponse("¡Bienvenido tareas!")

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear-tarea')
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})