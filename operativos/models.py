from django.db import models

# Create your models here.

class RecursoOperativo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    operativo_equipos = models.CharField(max_length=100, blank=True, null=True)
    operativo_materiales = models.CharField(max_length=100, blank=True, null=True)
    operativo_herramientas = models.CharField(max_length=100, blank=True, null=True)
    operativo_manodeobra = models.CharField(max_length=100, blank=True, null=True)
    operativo_epps = models.CharField(max_length=100, blank=True, null=True)
    operativo_generales = models.CharField(max_length=100, blank=True, null=True)

    # Otros campos relevantes para los recursos operativos

    def __str__(self):
        campos = [
            self.nombre or "sin nombre",
            self.operativo_equipos or "sin equipos",
            self.operativo_materiales or "sin materiales",
            self.operativo_herramientas or "sin herramientas",
            self.operativo_manodeobra or "sin manodeobra",
            self.operativo_epps or "sin epps",
            self.operativo_generales or "sin generales",
        ]
        return " | ".join(campos)