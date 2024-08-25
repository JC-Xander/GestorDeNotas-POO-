from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    MaestroViewSet, 
    MaestroDataViewSet, 
    MaestroAlumnosViewSet,
    MaestroAsignaturasViewSet,
    AlumnoViewSet,
    RetroalimentacionViewSet,
)

router = DefaultRouter()
router.register(r'maestros', MaestroViewSet, basename='maestros-completo')
router.register(r'maestrosData', MaestroDataViewSet, basename='maestros-data')
router.register(r'maestro-alumnos', MaestroAlumnosViewSet, basename='maestro-alumnos')
router.register(r'maestro-asignatura', MaestroAsignaturasViewSet, basename='maestro-asignatura' )
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'retroalimentacion', RetroalimentacionViewSet, basename='retroalimentacion')

urlpatterns = [
    path('', include(router.urls))
]

