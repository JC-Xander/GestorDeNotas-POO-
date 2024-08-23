from rest_framework import serializers
from .models import Maestro, Alumno
from Edificio.serializers import AulaSerializer

class MaestroSerializer(serializers.ModelSerializer):
    aula = AulaSerializer()

    class Meta:
        model = Maestro
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    maestro = MaestroSerializer()

    class Meta:
        model = Alumno
        fields = '__all__'



