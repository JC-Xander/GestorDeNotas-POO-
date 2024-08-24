from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import (
    AsignaturaViewSet,
    BimestreViewSet,
    PlanEstudioViewSet
)

router = DefaultRouter()
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'bimestres', BimestreViewSet)
router.register(r'planEstudio', PlanEstudioViewSet)

urlpatterns = [
    path('', include(router.urls))
]

