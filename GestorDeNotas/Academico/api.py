from rest_framework import viewsets

from .models import (
    Asignatura,
    Bimestre,
    PlanEstudio,
)
from .serializers import (
    AsignaturaSerializer,
    BimestreSerializer,
    PlanEstudioSerializer,
)
# ----- ViewSet Asignatura ------
class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

# ----- ViewSet Bimestre ------
class BimestreViewSet(viewsets.ModelViewSet):
    queryset = Bimestre.objects.all()
    serializer_class = BimestreSerializer

# ----- ViewSet PlanEstudio ------
class PlanEstudioViewSet(viewsets.ModelViewSet):
    queryset = PlanEstudio.objects.all()
    serializer_class = PlanEstudioSerializer

