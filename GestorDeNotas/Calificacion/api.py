from rest_framework import viewsets

from .models import (
    Evaluacion,
    Calificacion,
)
from .serializers import (
    EvaluacionSerializer,
    CalificacionSerializer,
)

# ------- views Evaluacion -----
class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

# ------ views Calificacion -----
class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

