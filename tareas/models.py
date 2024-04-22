from django.db import models
from procesos.models import Subproceso
from seguridad.models import RecursoSeguridad
from calidad.models import RecursoCalidad
from operativos.models import RecursoOperativo

# Create your models here.
class Tarea(models.Model):
    subproceso = models.ManyToManyField(Subproceso, related_name='tareas')
    verbo = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    recurso_seguridad = models.ManyToManyField(RecursoSeguridad, related_name='tareas', blank=True)
    recurso_calidad = models.ManyToManyField(RecursoCalidad, related_name='tareas', blank=True)
    recurso_operativo = models.ManyToManyField(RecursoOperativo, related_name='tareas', blank=True)
    unidad_de_medida = models.CharField(max_length=50, default='minutos', blank=True)  # Un valor por defecto lógico y permitir vacío
    tiempo_tarea = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Permitir nulos y vacíos
  # Asume que quieres ser preciso hasta centésimos, ajusta según necesites


    def __str__(self):
        return f"{self.verbo} {self.objeto}"