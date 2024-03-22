





from django.http import HttpResponse

def vista_simple(request):
    return HttpResponse("Hola, esta es una respuesta simple desde modelos.")
