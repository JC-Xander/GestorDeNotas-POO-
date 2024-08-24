# Edificio/urls.py
from django.urls import path, include
from .api import router  # Importa el router en lugar de los ViewSets

urlpatterns = [
    path('', include(router.urls)),
]

