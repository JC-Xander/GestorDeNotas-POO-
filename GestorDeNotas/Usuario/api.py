# Vistas de la Rest API
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    status
)
from .models import (   
    Maestro,
    Alumno,
)
from .serializers import (
    MaestroSerializer,
    MaestroDataSerializer,
    MaestroAlumnosSerializer,
    MaestroAsignaturasSerializer,
    AlumnoSerializer,
    RetroalimetacionSerializer,
)

# ----- ViewSet Maestro ------
class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer


class MaestroDataViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroDataSerializer

class MaestroAlumnosViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroAlumnosSerializer

class MaestroAsignaturasViewSet(viewsets.ModelViewSet):
    def list(self, request):
        """Obtiene las asignaturas del maestro basadas en el bimestre."""
        bimestre = request.query_params.get('bimestre')
        if not bimestre:
            return Response({"detail": "El parámetro 'bimestre' es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            bimestre_id = int(bimestre)
        except ValueError:
            return Response({"detail": "El parámetro 'bimestre' debe ser un número entero."}, status=status.HTTP_400_BAD_REQUEST)

        maestros = Maestro.objects.all()
        serializer = MaestroAsignaturasSerializer(maestros, context={'bimestre': bimestre_id}, many=True)

        response_data = {
            'bimestre': bimestre_id,
            'asignaturas': serializer.data
        }

        return Response(response_data)
    

class RetroalimentacionViewSet(viewsets.ViewSet):
    """
    ViewSet para obtener todos los maestros con calificaciones basadas en un bimestre específico.
    """

    queryset = Maestro.objects.all()
    serializer_class = RetroalimetacionSerializer

    def get_serializer_context(self):
        """
        Añade el bimestre al contexto del serializer.
        """
        context = super().get_serializer_context()
        bimestre = self.request.query_params.get('bimestre')
        if bimestre:
            try:
                context['bimestre'] = int(bimestre)
            except ValueError:
                context['bimestre'] = None
        else:
            context['bimestre'] = None
        return context
    

# ----- ViewSet Alumno ------
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer



