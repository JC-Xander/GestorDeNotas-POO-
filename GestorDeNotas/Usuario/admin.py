from django.contrib import admin

# Register your models here.
from .models import Maestro, Alumno

@admin.register(Maestro)
class MaestroAdmin(admin.ModelAdmin):
    pass

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass
