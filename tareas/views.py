from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    return HttpResponse("¡Bienvenido tareas!")