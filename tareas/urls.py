from django.urls import path
from . import views

urlpatterns = [
    path('crear-tarea/', views.crear_tarea, name='crear-tarea'),
    # Puedes agregar más rutas aquí
]
