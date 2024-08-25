from django.db import models
from Edificio.models import Aula


class Persona(models.Model):
    """Modelo que representa a todos los usuarios, almacenando sus datos principales"""
    # ----- Generos -----
    MASCULINO = 1
    FEMENINO = 2
    NO_ESPECIFICADO = 3

    GENDER_CHOISE = (
        (MASCULINO, 'Maculino'),
        (FEMENINO, 'Femenino'),
        (NO_ESPECIFICADO, 'No especificado'),
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
        return f"{self.nombre_completo}"
    
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
    telefono = models.CharField('Telefono', max_length=10)
    aula = models.OneToOneField(
        Aula,
        on_delete=models.PROTECT,
        related_name='aula',
    )


    class Meta:
        db_table = 'Maestros'

    # ------ METODOS -----
    
    def contar_alumnos(self) -> int:
        """Retorna el total del alumnos del maestro"""
        return self.alumnos.count()

    #==================================================================================================

    def asignaturas_bimestrales(self, bimestre_id:int) -> list:
        """Lista todas las asignaturas que el maestro imparte en un bimestre"""

        from Academico.models import PlanEstudio

        asignaturas = PlanEstudio.objects.filter(
            maestro=self,
            bimestre=bimestre_id
        ).values_list('clase__nombre', flat=True).distinct()
        return list(asignaturas)
    
    def calificaciones_asignatura(self, bimestre_id: int) -> dict:
        """
        Lista todas las calificaciones de los alumnos asignados a este maestro, por asignatura y bimestre.
        """
        from Academico.models import PlanEstudio
        from Calificacion.models import Evaluacion, Calificacion

        # Filtra los planes de estudio para el maestro y el bimestre especificado
        planes = PlanEstudio.objects.filter(maestro=self, bimestre=bimestre_id)

        calificaciones_asignatura = {}  # Diccionario para almacenar las calificaciones

        for plan in planes:
            # Filtra las evaluaciones relacionadas con el plan de estudio
            evaluaciones = Evaluacion.objects.filter(plan_estudio=plan)

            # Filtra las calificaciones basadas en evaluaciones y alumnos del maestro
            calificaciones = Calificacion.objects.filter(
                evaluacion=evaluaciones,
                alumno=self.alumnos.all()
            ).values(
                'alumno__nombre', 'alumno__apellido', 'evaluacion__titulo', 'calificacion'
            )

            asignatura_nombre = plan.clase.nombre
            if asignatura_nombre not in calificaciones_asignatura:
                calificaciones_asignatura[asignatura_nombre] = []

            for calificacion in calificaciones:
                calificaciones_asignatura[asignatura_nombre].append({
                    'alumno': f"{calificacion['alumno__nombre']} {calificacion['alumno__apellido']}",
                    'evaluacion': calificacion['evaluacion__titulo'],
                    'calificacion': calificacion['calificacion']
                })

        return calificaciones_asignatura

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





