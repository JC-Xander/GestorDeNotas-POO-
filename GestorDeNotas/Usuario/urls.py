from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    MaestroViewSet, 
    MaestroDataViewSet, 
    MaestroAlumnosViewSet,
    AlumnoViewSet,
)

router = DefaultRouter()
router.register(r'maestros', MaestroViewSet, basename='maestros-completo')
router.register(r'maestrosData', MaestroDataViewSet, basename='maestros-data')
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'maestro-alumnos', MaestroAlumnosViewSet, basename='maestro-asignatura')

urlpatterns = [
    path('', include(router.urls))
]

