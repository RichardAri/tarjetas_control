from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

"""
# Create your models here.
class TarjetaDeControl(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    valorizacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    tareas = models.ManyToManyField('Tarea', related_name='tarjetas_de_control')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarjetas_de_control')

    def __str__(self):
        return self.titulo

    @property
    def num_tareas(self):
        return self.tareas.count(
            """
