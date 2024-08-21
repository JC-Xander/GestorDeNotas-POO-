from django.contrib import admin
from .models import Escuela, Aula

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_filter = ["codigo"]
