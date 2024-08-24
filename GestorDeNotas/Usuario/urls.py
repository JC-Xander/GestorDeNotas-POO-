from django.urls import path, include

from rest_framework.routers import DefaultRouter

from.api import (
    MaestroViewSet,
    MaestroDataViewSet,
    AlumnoViewSet,
) 

router = DefaultRouter()
router.register(r'maestros', MaestroViewSet)
router.register(r'maestrosData', MaestroDataViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
