# Edificio/serializers.py
from rest_framework import serializers
from .models import Escuela, Aula

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    escuela = EscuelaSerializer()

    class Meta:
        model = Aula
        fields = '__all__'




