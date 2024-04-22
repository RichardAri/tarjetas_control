
"""
class RecursoSeguridad(models.Model):
    clase_seguridad = models.CharField(max_length=100, blank=True, null=True)
    seguridad_peligro = models.CharField(max_length=100, blank=True, null=True)
    seguridad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    seguridad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de seguridad
    def __str__(self):
        return self.seguridad_peligro or "Recurso de Seguridad sin nombre"

class RecursoCalidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    calidad_peligro = models.CharField(max_length=100, blank=True, null=True)
    calidad_riesgo = models.CharField(max_length=100, blank=True, null=True)
    calidad_causas = models.CharField(max_length=100, blank=True, null=True)
    calidad_control = models.CharField(max_length=100, blank=True, null=True)
    # Otros campos relevantes para los recursos de calidad
    def __str__(self):
        return self.calidad_peligro or "Recurso de Calidad sin nombre"

class RecursoOperativo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    operativo_equipos = models.CharField(max_length=100, blank=True, null=True)
    operativo_materiales = models.CharField(max_length=100, blank=True, null=True)
    operativo_herramientas = models.CharField(max_length=100, blank=True, null=True)
    operativo_manodeobra = models.CharField(max_length=100, blank=True, null=True)
    operativo_epps = models.CharField(max_length=100, blank=True, null=True)
    operativo_generales = models.CharField(max_length=100, blank=True, null=True)

    # Otros campos relevantes para los recursos operativos

    def __str__(self):
        campos = [
            self.nombre or "sin nombre",
            self.operativo_equipos or "sin equipos",
            self.operativo_materiales or "sin materiales",
            self.operativo_herramientas or "sin herramientas",
            self.operativo_manodeobra or "sin manodeobra",
            self.operativo_epps or "sin epps",
            self.operativo_generales or "sin generales",
        ]
        return " | ".join(campos)

class Tarea(models.Model):
    subproceso = models.ManyToManyField(Subproceso, related_name='tareas')
    verbo = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    recurso_seguridad = models.ManyToManyField(RecursoSeguridad, related_name='tareas', blank=True)
    recurso_calidad = models.ManyToManyField(RecursoCalidad, related_name='tareas', blank=True)
    recurso_operativo = models.ManyToManyField(RecursoOperativo, related_name='tareas', blank=True)
    unidad_de_medida = models.CharField(max_length=50, default='minutos', blank=True)  # Un valor por defecto lógico y permitir vacío
    tiempo_tarea = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Permitir nulos y vacíos
  # Asume que quieres ser preciso hasta centésimos, ajusta según necesites


    def __str__(self):
        return f"{self.verbo} {self.objeto}"

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
        return self.tareas.count()


    
    # Más métodos y propiedades según sea necesario
"""