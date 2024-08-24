from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import (
    AsignaturaViewSet,
    BimestreViewSet,
    PlanEstudioViewSet
)

router = DefaultRouter()
router.register(r'Asignaturas', AsignaturaViewSet)
router.register(r'Bimestres', BimestreViewSet)
router.register(r'PlanEstudio', PlanEstudioViewSet)

urlpatterns = [
    path('', include(router.urls))
]

