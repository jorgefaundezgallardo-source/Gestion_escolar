from rest_framework import serializers
from .models import Docente, Alumno, RegistroAcademico

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class RegistroAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcademico
        fields = '__all__'

    # Regla para Validar que la calificación esté en el rango chileno válido
    def validate_calificacion(self, value):
        if value < 1.0 or value > 7.0:
            raise serializers.ValidationError("Error de validación: La calificación debe estar entre 1.0 y 7.0")
        return value