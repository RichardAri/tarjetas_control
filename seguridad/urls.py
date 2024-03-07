from django.urls import path
from . import views

urlpatterns = [
    # HTMX
    path('', views.index, name='seguridad_index'),
    path('create-seguridad/', views.create_seguridad, name='create-seguridad')

]
