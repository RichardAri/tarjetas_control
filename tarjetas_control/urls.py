from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tarjetas_control'),
    # Puedes agregar más rutas aquí
]
