from django.contrib import admin

# Register your models here.
from .models import Evaluacion, Calificacion

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    pass

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    pass