from rest_framework import serializers
from .models import Maestro, Alumno

from Edificio.serializers import AulaSerializer

# ------ Serializer Maestro ----------
class MaestroSerializer(serializers.ModelSerializer):
    """Serializer con todos los datos de Maestro con los datos de sus respectivas relaciones"""

    aula = AulaSerializer()

    class Meta:
        model = Maestro
        fields = '__all__'

class MaestroAlumnosSerializer(serializers.ModelSerializer):
    """Serializa los datos del maestro incluyendo el conteo de alumnos"""

    alumnos = serializers.SerializerMethodField()

    class Meta:
        model = Maestro
        fields = ['nombre', 'apellido', 'aula', 'grado', 'seccion', 'alumnos']

    def get_alumnos(self, obj):
        """Obtiene el número de alumnos asignados al maestro"""
        return obj.contar_alumnos()
    
class MaestroAsignaturasSerializer(serializers.ModelSerializer):
    """Serializa los datos del maestro incluyendo las clases que impartira"""

    asignaturas = serializers.SerializerMethodField()

    class Meta:
        model = Maestro
        fields = ['nombre', 'apellido', 'grado', 'seccion', 'asignaturas']

    def get_asignaturas(self, obj):
        """Obtiene las Asignaturas del Maestro"""
        bimestre = self.context.get('bimestre')
        if bimestre:
            return obj.asignaturas_bimestrales(bimestre)
        return []

class MaestroDataSerializer(serializers.ModelSerializer):
    """Serializer unicamente los datos que almacena Maestro"""

    class Meta:
        model = Maestro
        fields = '__all__'

# ------ Serializer Alumno ----------
class AlumnoSerializer(serializers.ModelSerializer):
    """Serializer con todos los datos de Alumno y los del maestro asignado"""
    maestro = MaestroDataSerializer()
    # nota = serializers.SerializerMethodField()

    class Meta:
        model = Alumno
        fields = '__all__'



