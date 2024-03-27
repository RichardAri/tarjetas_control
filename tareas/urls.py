from django.urls import path
from . import views

urlpatterns = [
    path('crear-tarea/', views.crear_tarea, name='crear-tarea'),
    path('tareas/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tareas/', views.listar_tareas, name='listar_tareas'),
    path('editar-tarea/<int:tarea_id>/', views.editar_tarea, name='editar-tarea'),
    path('editar_tarea_nuevo/<int:tarea_id>/', views.editar_tarea_nuevo, name='editar_tarea_nuevo'),
  
    # Puedes agregar más rutas aquí
]
