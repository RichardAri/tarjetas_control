from django.urls import path
from . import views

urlpatterns = [
    # EQUIPOS
    path('', views.index, name='index_equipos'),
    path('create-equipo/', views.create_equipo, name='create-equipo'),
    
    # SERVICIOS
    path('crear-servicio/', views.crear_servicio, name='crear-servicio'),
    path('servicios/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicios/', views.listar_servicios, name='listar_servicios'),
    
    # dos para actualziar y eliinar un equipo dentro del servicio
    path('actualizar-cantidad-equipo/<int:equipo_id>/', views.actualizar_cantidad_equipo, name='actualizar_cantidad_equipo'),
    path('eliminar-equipo/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),


]
