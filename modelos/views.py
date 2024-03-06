from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Aquí puedes colocar cualquier lógica adicional que necesites
    return HttpResponse("¡Bienvenido modelos!")