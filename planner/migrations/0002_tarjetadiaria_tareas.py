# Generated by Django 5.0.3 on 2024-03-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0005_tarjetadecontrol_usuario'),
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjetadiaria',
            name='tareas',
            field=models.ManyToManyField(blank=True, related_name='tarjetas_diarias', to='modelos.tarea'),
        ),
    ]