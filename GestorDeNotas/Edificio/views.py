# Edificio/views.py
from rest_framework import viewsets
from .models import Escuela, Aula
from .serializers import EscuelaSerializer, AulaSerializer

class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer

class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

