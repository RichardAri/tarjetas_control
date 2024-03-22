from django.db import models

class Proceso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Subproceso(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, related_name='subprocesos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
 
