from django.db import models
from cuentas.models import UserProfile
from modelos.models import Tarea
from django.db.models import Sum


class TarjetaDiaria(models.Model):
    DURACION_JORNADA = [
        (8, '8 horas'),
        (12, '12 horas'),
    ]
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fecha = models.DateField()
    tareas = models.ManyToManyField(Tarea, related_name='tarjetas_diarias', blank=True)
    total_minutos = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    duracion_jornada = models.IntegerField(choices=DURACION_JORNADA, default=8)

    def calcular_total_minutos(self):
        if self.pk:
            total_minutos_tareas = self.tareas.aggregate(Sum('tiempo_tarea'))['tiempo_tarea__sum'] or 0
            return total_minutos_tareas
        return 0

    def save(self, *args, **kwargs):
        # Calcula total_minutos antes de guardar
        nuevos_total_minutos = self.calcular_total_minutos()
        # Guarda la instancia solo si es una nueva o si total_minutos ha cambiado
        if not self.pk or nuevos_total_minutos != self.total_minutos:
            self.total_minutos = nuevos_total_minutos
            super(TarjetaDiaria, self).save(*args, **kwargs)

    def horas_y_minutos(self):
        total_minutos = int(self.total_minutos)
        horas = total_minutos // 60
        minutos = total_minutos % 60
        return f"{horas}h {minutos}"

    def __str__(self):
        return f'Tarjeta de {self.usuario.user.username} - {self.fecha}'