from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='operativos_index'),
    path('recursos/', views.recursos_operativos, name='recurso_operativos'),
    #htmx
    path('create-form/', views.create_operativo, name = 'create-operativo')
]
