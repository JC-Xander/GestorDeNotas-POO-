from rest_framework import serializers

from .models import Evaluacion, Calificacion

from Academico.serializers import PlanEstudioSerializer

# ---- Serializers Evaluacion -------
class EvaluacionSerializer(serializers.ModelSerializer):
    plan_estudio = PlanEstudioSerializer()

    class Meta:
        model = Evaluacion
        fields = '__all__'

# ---- Serializers Calificación -------
class CalificacionSerializer(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer()

    class Meta:
        model = Calificacion
        fields = '__all__'



