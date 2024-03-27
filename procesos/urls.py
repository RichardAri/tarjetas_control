from django.urls import path
from .views import mi_vista_compleja, lista_procesos, lista_subprocesos, lista_tareas # Asegúrate de importar la vista correctamente

urlpatterns = [
    path('procesos/', mi_vista_compleja, name='procesos_sin_id'),
    path('procesos/<int:proceso_id>/', mi_vista_compleja, name='procesos_con_id'),
    #lista procesos
    path('lista_procesos/', lista_procesos, name='lista_procesos'),
    #lista de subprocesos
    path('lista_subprocesos/', lista_subprocesos, name='lista_subprocesos'),
    #lista de tareas
    path('lista_tareas/', lista_tareas, name='lista_tareas'),
]
