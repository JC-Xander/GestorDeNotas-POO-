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



