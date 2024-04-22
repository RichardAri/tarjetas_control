from django.db import models

# Create your models here.

class RecursoCalidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    calidad_peligro = models.CharField(max_length=100, blank=True, null=True)
    calidad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    calidad_causas = models.CharField(max_length=100, blank=True, null=True)
    calidad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de calidad
    def __str__(self):
        return self.calidad_peligro or "Recurso de Calidad sin nombre"