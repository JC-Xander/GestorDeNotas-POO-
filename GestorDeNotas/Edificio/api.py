# Edificio/api.py
from rest_framework.routers import DefaultRouter
from .views import EscuelaViewSet, AulaViewSet

router = DefaultRouter()
router.register(r'escuelas', EscuelaViewSet)  # usa minúsculas para la URL
router.register(r'aulas', AulaViewSet)        # usa minúsculas para la URL




