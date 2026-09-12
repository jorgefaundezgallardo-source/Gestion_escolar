from django.contrib import admin
from .models import Alumno, Docente, RegistroAcademico

# Registramos los modelos de forma directa para habilitar el CRUD
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(RegistroAcademico)