from django.db import models
from django.contrib.auth.models import User

class BugReport(models.Model):
    ESTADOS = (
        ('Nuevo', 'Nuevo'),
        ('En revisión', 'En revisión'),
        ('Resuelto', 'Resuelto'),
    )
    TIPO_DE_REPORTE = (
        ('Bug', 'Bug'),
        ('Mejora', 'Mejora'),
        ('Requerimiento', 'Requerimiento'),
    )
    tipo = models.CharField(max_length=15, choices=TIPO_DE_REPORTE, default='Bug')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Opcional
    description = models.TextField()
    image = models.ImageField(upload_to='bug_reports/', blank=True, null=True)  # Ruta donde se guardan las imágenes
    status = models.CharField(max_length=20, choices=ESTADOS, default='Nuevo')
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bug reportado por {self.user.username} el {self.date_reported}"
