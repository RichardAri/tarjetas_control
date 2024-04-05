from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

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

def crear_tarjetas_anuales(sender, instance, created, **kwargs):
    from planner.models import TarjetaDiaria
    if created:
        usuario = instance
        hoy = datetime.now().date()
        
        # Establecer el inicio en el primer día del mes actual
        fecha_inicio = hoy.replace(day=1)

        # La fecha de finalización sigue siendo un año después
        fecha_fin = fecha_inicio + relativedelta(years=1)

        # Crear tarjetas diarias desde el principio del mes
        fecha_actual = fecha_inicio
        while fecha_actual < fecha_fin:
            TarjetaDiaria.objects.get_or_create(usuario=usuario, fecha=fecha_actual)
            fecha_actual += timedelta(days=1)


