from django.db import models

from core import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class RecursoSeguridad(models.Model):
    clase_seguridad = models.CharField(max_length=100, blank=True, null=True)
    seguridad_peligro = models.CharField(max_length=100, blank=True, null=True)
    seguridad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    seguridad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de seguridad
    def __str__(self):
        return self.clase_seguridad or "Recurso de Seguridad sin nombre"

class RecursoCalidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    calidad_peligro = models.CharField(max_length=100, blank=True, null=True)
    calidad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    calidad_causas = models.CharField(max_length=100, blank=True, null=True)
    calidad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de calidad
    def __str__(self):
        return self.nombre or "Recurso de Calidad sin nombre"

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
        return self.nombre or "Recurso Operativo sin nombre"

class Tarea(models.Model):
    verbo = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    orden_de_venta = models.CharField(max_length=100, null=True, blank=True)
    recurso_seguridad = models.ForeignKey(RecursoSeguridad, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)
    recurso_calidad = models.ForeignKey(RecursoCalidad, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)
    recurso_operativo = models.ForeignKey(RecursoOperativo, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)
class TarjetaDeControl(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    valorizacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    tareas = models.ManyToManyField('Tarea', related_name='tarjetas_de_control')

    def __str__(self):
        return self.titulo

    @property
    def num_tareas(self):
        return self.tareas.count()

    
    # Más métodos y propiedades según sea necesario
