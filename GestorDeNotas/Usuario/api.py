# Vistas de la Rest API
# from rest_framework.response import Response
from rest_framework import (
    viewsets,
)
from .models import (   
    Maestro,
    Alumno,
)
from .serializers import (
    MaestroSerializer,
    MaestroDataSerializer,
    AlumnoSerializer,
)

# ----- ViewSet Maestro ------
class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer


class MaestroDataViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroDataSerializer


# ----- ViewSet Alumno ------
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer



