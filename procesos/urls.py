from django.urls import path
from .views import mi_vista_compleja  # Asegúrate de importar la vista correctamente

urlpatterns = [
    path('', mi_vista_compleja, name='nombre_de_mi_vista'),
]
