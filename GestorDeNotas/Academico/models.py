from django.db import models
import datetime

# Create your models here.
from Usuario.models import Maestro

class Asignatura(models.Model):
    """Representa las clases que se imparten"""

    nombre = models.CharField('Nombre de la clase', max_length=30, unique=True)
    codigo = models.CharField('Codigo de la clase', max_length=5, unique=True)

    class Meta:
        db_table = 'Asignaturas'

    # ------ METODOS ------

    def __str__(self):
        return f"{self.nombre}"

# ----------------------------------

class Bimestre(models.Model):
    """Representa el bimestre actual"""

    # ---- Semestres ----
    BIMESTRE_CHOICE = (
        ('I', 'Primer semestre'),
        ('II', 'Segundo bimestre'),
    )
    # -----------------------------

    anio = models.PositiveIntegerField(default=datetime.date.today().year, editable=False)
    n_bimestre = models.CharField(
        'bimestre',
        choices=BIMESTRE_CHOICE,
        max_length=2,
    )

    class Meta:
        db_table='Bimestres'
        constraints=[
            models.UniqueConstraint(fields=['anio', 'n_bimestre'], name='No pueden haber dos semestres iguales en un mismo año')
        ]

    # ------- METODOS ------
    def __str__(self):
        return f'{self.n_bimestre} {self.anio}'
    
# ------------------------------------

class PlanEstudio(models.Model):
    """Representa las clases que impartira el docente en x semestre"""

    maestro = models.ForeignKey(
        Maestro,
        on_delete=models.CASCADE,
        related_name='plan'
    )
    clase = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='plan'
    )
    bimestre = models.ForeignKey(
        Bimestre,
        on_delete=models.CASCADE,
        related_name='plan_estudio'
    )

    class Meta:
        db_table = 'Planes'
        constraints = [
            models.UniqueConstraint(fields=['maestro', 'clase', 'bimestre'], name='Un maestro no puede llevar clases repetidas en el mismo bimestre')
        ]

    # ------ METODOS -------

    def __str__(self):
        return f'{self.maestro} - {self.clase}'
    
# ----------------------------------
