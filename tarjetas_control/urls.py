from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tarjetas_control'),
    # Puedes agregar más rutas aquí
    path('tarjeta-control/crear/', views.crear_editar_tarjeta_control, name='crear_tarjeta_control'),
    path('tarjeta-control/editar/<int:tarjeta_id>/', views.crear_editar_tarjeta_control, name='editar_tarjeta_control'),
    path('tarjetas-control/', views.listar_tarjetas_control, name='listar_tarjetas_control'),
    path('tarjeta-control/<int:tarjeta_id>/', views.detalle_tarjeta_control, name='detalle_tarjeta_control'),



]
