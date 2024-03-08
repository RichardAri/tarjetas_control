# Generated by Django 5.0.3 on 2024-03-08 20:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_remove_tarea_recurso_calidad_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjetadecontrol',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tarjetas_de_control', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
