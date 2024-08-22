from django.db import models
from django.utils import timezone

# Create your models here.
from Academico.models import PlanEstudio

class Evaluacion(models.Model): 
    """Tareas creadas por el maestro"""

    # ------- Parciales -------
    PRIMER_PARCIAL = 1
    SEGUNDO_PARCIAL = 2
    TERCER_PARCIAL = 3
    CUARTO_PARCIAL = 4

    PARCIAL_CHOICE=(
        (PRIMER_PARCIAL, 'Primer parcial'),
        (SEGUNDO_PARCIAL, 'Segundo parcial'),
        (TERCER_PARCIAL, 'Tercer parcial'),
        (CUARTO_PARCIAL, 'Cuarto parcial')
    )
    # ------------------------------------

    titulo = models.CharField('titulo', max_length=200)
    descripcion = models.TextField('descripción')
    valor = models.PositiveSmallIntegerField('valor de la tarea', default=0)
    fecha_inicio = models.DateTimeField('Fecha de Inicio', default=timezone.now)
    fecha_cierre = models.DateTimeField('Fecha de cierre', null=True, blank=True)
    archivo_adjunto = models.FileField(
        'archivo adjunto', 
        upload_to='archivosEvaluacion/', 
        null=True,
        blank=True
    )
    parcial = models.PositiveIntegerField(
        'Parcial',
        choices=PARCIAL_CHOICE,
        default=PRIMER_PARCIAL
    )

    class Meta:
        db_table='Evaluaciones'

    # ------ METODOS ------

# --------------------------------------


