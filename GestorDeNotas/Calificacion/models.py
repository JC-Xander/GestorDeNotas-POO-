from django.db import models
from django.utils import timezone

# Create your models here.
from Academico.models import PlanEstudio
from Usuario.models import Alumno

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
    plan_estudio = models.ForeignKey(
        PlanEstudio,
        on_delete=models.CASCADE,
        related_name='evaluaciones',
        verbose_name='Plan de Estudio'
    )
    parcial = models.PositiveIntegerField(
        'Parcial',
        choices=PARCIAL_CHOICE,
        default=PRIMER_PARCIAL
    )
    archivo_adjunto = models.FileField(
        'archivo adjunto', 
        upload_to='archivosEvaluacion/', 
        null=True,
        blank=True
    )

    class Meta:
        db_table='Evaluaciones'

    # ------ METODOS ------

# --------------------------------------

class Calificacion(models.Model):
    """Almacena todas las calificaciones del estudiante"""

    # ------ Estados ------
    PENDIENTE = 1
    REVISION = 2
    ENTREGADO = 3
    NO_ENTREGADO = 4

    ESTADOS_CHOICES = (
        (PENDIENTE, 'Tarea pendiente'),
        (REVISION , 'Tarea en revició'),
        (ENTREGADO, 'Tarea entregada'),
        (NO_ENTREGADO, 'Tarea no entregada')
    )
    # --------------------------------

    evaluacion = models.ForeignKey(
        Evaluacion,
        on_delete=models.CASCADE,
        related_name='calificaciones',
        verbose_name='Evaluacion'
    )
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='calificaciones',
        verbose_name='alumno'
    )
    calificacion = models.PositiveSmallIntegerField('Calificación', default=0)
    estado = models.PositiveIntegerField(
        'Estado actual',
        choices=ESTADOS_CHOICES,
        default=PENDIENTE
    )
    evidencia = models.FileField(
        'Evidencia de la tarea',
        upload_to='archivosCalificacion/',
        null=True,
        blank=True
    )

    class Meta:
        db_table='Calificaciones'
        constraints=[
            models.UniqueConstraint(fields=['evaluacion', 'alumno'], name='Un alumno no puede tene 2 califícaciones de la misma tarea')
        ]

    # ------ METODOS ------

# ------------------------------------