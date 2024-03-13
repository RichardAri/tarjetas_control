from django.urls import path
from . import views

urlpatterns = [
    # EQUIPOS
    path('', views.index, name='index_equipos'),
    path('create-equipo/', views.create_equipo, name='create-equipo'),
    
    # SERVICIOS
    path('crear-servicio/', views.crear_servicio, name='crear-servicio'),
    path('servicios/<int:tservicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicios/', views.listar_servicios, name='listar_servicios'),
]
