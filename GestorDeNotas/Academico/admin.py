from django.contrib import admin

# Register your models here.
from .models import Asignatura, Bimestre, PlanEstudio

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    pass

@admin.register(Bimestre)
class BimestreAdmin(admin.ModelAdmin):
    pass

@admin.register(PlanEstudio)
class PlanEstudioAdmin(admin.ModelAdmin):
    pass