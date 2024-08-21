from django.db import models
from Usuario.models import Maestro

class Escuela(models.Model):
    """Modelo que representará al centro educativo"""
    
    nombre = models.CharField("nombre", max_length=100)
    direccion = models.TextField("direccion")
    telefono = models.JSONField(default=list)
    director = models.OneToOneField(
        Maestro,
        on_delete=models.PROTECT,
        related_name='isDirector'
    )

    class Meta:
        db_table = 'Escuelas'
        verbose_name = 'escuela'
        verbose_name_plural = 'escuelas'

    # ------ METODOS -------

# ---------------------------

class Aula(models.Model):
    """Representa las aulas del centro educativo"""

    Codigo = models.CharField('Codigo Aula', max_length=15)

    class Meta:
        db_table = 'Aula'
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'

    # ----- METODOS -----

# ----------------------------------------