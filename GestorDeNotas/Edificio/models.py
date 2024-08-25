from django.db import models

class Escuela(models.Model):
    """Modelo que representará al centro educativo"""
    
    nombre = models.CharField("nombre", max_length=100)
    direccion = models.TextField("direccion")
    telefono = models.JSONField(default=list)

    class Meta:
        db_table = 'Escuelas'
        verbose_name = 'escuela'
        verbose_name_plural = 'escuelas'

    # ------ METODOS -------

    def __str__(self):
        return self.nombre

# ---------------------------

class Aula(models.Model):
    """Representa las aulas del centro educativo"""

    codigo = models.CharField('Codigo Aula', max_length=15, unique=True)
    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.CASCADE,
        related_name='aulas',
    )

    class Meta:
        db_table = 'Aula'
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'

    # ----- METODOS -----
    def __str__(self):
        return self.codigo
# ----------------------------------------