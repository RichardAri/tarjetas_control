from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='calidad_index'),
    path('recursos/', views.recursos_calidad, name='recurso_calidad'),
    #htmx
    path('create-form/', views.create_recurso, name='create-recurso')
]
