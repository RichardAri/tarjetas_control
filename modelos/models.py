from django.db import models

class RecursoSeguridad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    seguridad_peligro = models.CharField(max_length=100, blank=True, null=True)
    seguridad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    seguridad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de seguridad

class RecursoCalidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    calidad_peligro = models.CharField(max_length=100, blank=True, null=True)
    calidad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    calidad_causas = models.CharField(max_length=100, blank=True, null=True)
    calidad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de calidad

class RecursoOperativo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    operativo_equipos = models.CharField(max_length=100, blank=True, null=True)
    operativo_materiales = models.CharField(max_length=100, blank=True, null=True)
    operativo_herramientas = models.CharField(max_length=100, blank=True, null=True)
    operativo_manodeobra = models.CharField(max_length=100, blank=True, null=True)
    operativo_epps = models.CharField(max_length=100, blank=True, null=True)
    operativo_generales = models.CharField(max_length=100, blank=True, null=True)

    # Otros campos relevantes para los recursos operativos

class Tarea(models.Model):
    verbo = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    orden_de_venta = models.CharField(max_length=100, null=True, blank=True)
    recurso_seguridad = models.ForeignKey(RecursoSeguridad, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)
    recurso_calidad = models.ForeignKey(RecursoCalidad, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)
    recurso_operativo = models.ForeignKey(RecursoOperativo, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)

