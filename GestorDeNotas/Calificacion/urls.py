from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import (
    EvaluacionViewSet,
    CalificacionViewSet,
)

router = DefaultRouter()
router.register(r'Evaluaciones', EvaluacionViewSet)
router.register(r'Calificaciones', CalificacionViewSet)

urlpatterns = [
    path('', include(router.urls))
]