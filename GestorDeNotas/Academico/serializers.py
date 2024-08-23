from rest_framework import serializers
from .models import Asignatura, Bimestre, PlanEstudio

# ----- Serializer de Asignatura ------- 
class AsignaturaSerializer(serializers.ModelSerializer):
    """serializer de todos los datos de Asignatura"""

    class Meta:
        model = Asignatura
        fields = '__all__'

# ----- Serializer de Bimestre ------- 
class BimestreSerializer(serializers.ModelSerializer):
    """serializer de todos los datos de Bimestre"""

    class Meta:
        model = Bimestre
        fields = '__all__'

# ----- Serializer PlanEstudio ---------
class PlanEstudioSerializer(serializers.ModelSerializer):
    """serializer de todos los datos de PlanEstudio"""

    clase = AsignaturaSerializer()
    bimestre = BimestreSerializer()

    class Meta:
        model = PlanEstudio
        fields = '__all__'




