from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import ListaOrdenVentaAPIView

urlpatterns = [
    path('', views.index_planner, name='index_planner'),
    path('tarjetas/', views.ver_tarjetas_diarias, name='ver_tarjetas_diarias'),
    # modal para crear las tarjetas segun el dia
    path('tarjetas-diarias/formulario', views.crear_o_editar_tarjeta_diaria, name='cargar_formulario_tarjeta_diaria'),
    path('tarjetas-diarias/guardar', views.crear_o_editar_tarjeta_diaria, name='guardar_tarjeta_diaria'),

    #prueba
    path('tarjetas-diarias/editar/<int:tarjeta_id>/', views.editar_tarjeta_diaria, name='editar_tarjeta_diaria'),
    # prueva de hoover
    path('tarjetas/<int:tarjeta_id>/', views.tareas_por_tarjeta, name='tareas_por_tarjeta'),
    path('tarjeta-diaria/<int:id>/', views.tarjeta_diaria_detail, name='tarjeta-diaria-detail'),

    # consumo api rest:
    path('api/', ListaOrdenVentaAPIView.as_view(), name='ordenesventa-lista'),
    
]
    
