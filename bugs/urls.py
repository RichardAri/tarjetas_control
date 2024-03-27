from django.urls import path
from . import views

urlpatterns = [
    # Otras URLs de tu app de bugs
    path('reportar/', views.report_bug, name='reportar-bug'),  # Añade esta línea para tu vista de reporte de bugs
]
