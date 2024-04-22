from django.db import models

# Create your models here.
class RecursoSeguridad(models.Model):
    clase_seguridad = models.CharField(max_length=100, blank=True, null=True)
    seguridad_peligro = models.CharField(max_length=100, blank=True, null=True)
    seguridad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    seguridad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de seguridad
    def __str__(self):
        return self.seguridad_peligro or "Recurso de Seguridad sin nombre"