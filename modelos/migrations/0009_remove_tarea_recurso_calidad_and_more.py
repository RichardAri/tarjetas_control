# Generated by Django 5.0.3 on 2024-04-22 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0008_remove_tarea_subproceso_tarea_subproceso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='recurso_calidad',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='recurso_operativo',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='recurso_seguridad',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='subproceso',
        ),
        migrations.RemoveField(
            model_name='tarjetadecontrol',
            name='tareas',
        ),
        migrations.RemoveField(
            model_name='tarjetadecontrol',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='RecursoCalidad',
        ),
        migrations.DeleteModel(
            name='RecursoOperativo',
        ),
        migrations.DeleteModel(
            name='RecursoSeguridad',
        ),
    ]