from django.db import models
from cuentas.models import UserProfile
from modelos.models import Tarea

class TarjetaDiaria(models.Model):
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fecha = models.DateField()
    tareas = models.ManyToManyField(Tarea, related_name='tarjetas_diarias', blank=True)
    # Otros campos de la tarjeta diaria
    def __str__(self):
        return f'Tarjeta de {self.usuario.user.username} - {self.fecha}'