from django.urls import path
from . import views
from .views import index, recurso_seguridad_create, recurso_seguridad_update, recurso_seguridad_delete


urlpatterns = [
    path('recursos/', views.recursos_seguridad, name='recurso_seguridad'),

    # HTMX
    path('', index, name='recurso-seguridad-list'),
    path('create/', recurso_seguridad_create, name='recurso-seguridad-create'),
    path('update/<int:pk>/', recurso_seguridad_update, name='recurso-seguridad-update'),
    path('delete/<int:pk>/', recurso_seguridad_delete, name='recurso-seguridad-delete'),
    # End of htmx

]
