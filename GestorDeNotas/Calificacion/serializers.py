from rest_framework import serializers

from .models import Evaluacion, Calificacion

from Academico.serializers import PlanEstudioSerializer
from Usuario.serializers import AlumnoSerializer

class EvaluacionSerializer(serializers.ModelSerializer):
    plan_estudio = PlanEstudioSerializer()

    class Meta:
        model = Evaluacion
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer()
    alumno = AlumnoSerializer()

    class Meta:
        model = Calificacion
        fields = '__all__'



