from django.urls import path
from . import views

urlpatterns = [
    #htmx
    path('', views.index, name='operativos_index'),
    path('create-form/', views.create_operativo, name = 'create-operativo')
]
