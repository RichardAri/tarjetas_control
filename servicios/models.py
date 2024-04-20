from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField(default=0)  # Agregar campo cantidad con valor predeterminado de 0


    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    ESTADO_CHOICES = [
        ('en_curso', 'En curso'),
        ('terminado', 'Terminado'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    equipos_necesarios = models.ManyToManyField(Equipo)
    supervisor = models.CharField(max_length=100)
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_curso')

    def __str__(self):
        return self.nombre