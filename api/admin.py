from django.contrib import admin
from .models import Alumno, Docente, RegistroAcademico

# Configuración visual para la tabla Alumno
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'curso', 'estado_matricula')
    search_fields = ('rut', 'apellido')
    list_filter = ('curso', 'estado_matricula')

# Configuración visual para la tabla Docente
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'especialidad', 'activo')
    search_fields = ('rut', 'apellido', 'especialidad')
    list_filter = ('activo',)

# Configuración visual para la tabla Registro Académico
class RegistroAcademicoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'asignatura', 'calificacion', 'docente', 'fecha_registro')
    search_fields = ('alumno__rut', 'asignatura')
    list_filter = ('asignatura', 'fecha_registro')

# Registramos los modelos en el panel de control
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(RegistroAcademico, RegistroAcademicoAdmin)