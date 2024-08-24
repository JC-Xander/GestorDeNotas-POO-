from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    MaestroViewSet, 
    MaestroDataViewSet, 
    AlumnoViewSet,
)

router = DefaultRouter()
router.register(r'maestros', MaestroViewSet, basename='maestros-completo')
router.register(r'maestrosData', MaestroDataViewSet, basename='maestros-data')
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')

urlpatterns = [
    path('', include(router.urls))
]

