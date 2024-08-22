from django.db import models
from Edificio.models import Aula


class Persona(models.Model):
    """Modelo que representa a todos los usuarios, almacenando sus datos principales
    """
    # ----- Generos -----
    MASCULINO = 1
    FEMENINO = 2
    OTRO = 3
    HELICOPTERO = 4
    MOTOR = 5
    NO_ESPECIFICADO = 6

    GENDER_CHOISE = (
        (MASCULINO, 'Maculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Gay'),
        (HELICOPTERO, 'Helicptero Apache'),
        (MOTOR, 'Motor de Lancha'),
        (NO_ESPECIFICADO, 'No especificado')
    )
    # ---------------------------

    nombre = models.CharField('nombre', max_length=100)
    apellido = models.CharField('apellido', max_length=100)
    genero = models.PositiveSmallIntegerField(
        'genero',
        choices=GENDER_CHOISE,
        default=NO_ESPECIFICADO,
    )
    direccion = models.TextField('dirección')
    correoInstitucional = models.EmailField('Correo', unique=True)
    
    class Meta:
        abstract = True

    # ------ METODOS -----

    def __str__(self):
        return f"{self.nombre_completo()} : {self.correoInstitucional}"
    
    @property
    def nombre_completo(self)-> str:
        """Retorna el mombre completo de la persona
        """
        return f"{self.nombre} {self.apellido}"
    

# --------------------------------------

class Maestro(Persona):
    """Representa a los Maestro de la escuela."""
    
    # ----- Grados ----- 
    GRADO_CHOICE = (
        (1, 'Primero'),
        (2, 'Segundo'),
        (3, 'Tercero'),
        (4, 'Cuarto'),
        (5, 'Quinto'),
        (6, 'Sexto'),
    )
    # ---------------------------
    grado = models.PositiveIntegerField(
        'grado',
        choices=GRADO_CHOICE,
        null=False,
        blank=False,
    )
    seccion = models.PositiveIntegerField('Seccion')
    aula = models.OneToOneField(
        Aula,
        on_delete=models.PROTECT,
        related_name='aula',
    )

    class Meta:
        db_table = 'Maestros'

    # ------ METODOS -----

# --------------------------------------------

class Alumno(Persona):
    """Representa a los alumnos de la escuela"""

    nombre_tutor = models.CharField('nombre del tutor', max_length=100)
    apellido_tutor = models.CharField('apellido del tutor', max_length=100)
    telefono_tutor = models.CharField('telefono del tutor', max_length=10)
    maestro = models.ForeignKey(
        Maestro,
        on_delete=models.SET_NULL,
        null=True,
        related_name='alumnos'
    )

    class Meta:
        db_table='Alumnos'

    # ------ METODOS -----
# ----------------------------------------------





