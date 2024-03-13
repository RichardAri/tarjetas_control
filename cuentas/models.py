from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import calendar

class UserProfile(models.Model):
    ROLES = (
        ('empleado', 'Empleado'),
        ('jefe', 'Jefe'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=100, choices=ROLES)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=UserProfile)
def crear_tarjetas_diarias(sender, instance, created, **kwargs):
    from planner.models import TarjetaDiaria  # Movemos la importación aquí
    if created:  # Solo ejecutar si se crea un nuevo usuario
        usuario = instance
        fecha_hoy = datetime.now()
        numero_dias_mes = calendar.monthrange(fecha_hoy.year, fecha_hoy.month)[1]
        for dia in range(1, numero_dias_mes + 1):
            fecha = datetime(fecha_hoy.year, fecha_hoy.month, dia).date()
            TarjetaDiaria.objects.create(usuario=usuario, fecha=fecha)

        # Si deseas eliminar las tarjetas de días anteriores descomenta la siguiente línea
        # eliminar_tarjetas_anteriores(usuario)

def eliminar_tarjetas_anteriores(usuario):
    from planner.models import TarjetaDiaria  # También movemos la importación aquí
    fecha_hoy = datetime.now()
    TarjetaDiaria.objects.filter(usuario=usuario, fecha__lt=datetime(fecha_hoy.year, fecha_hoy.month, 1)).delete()
