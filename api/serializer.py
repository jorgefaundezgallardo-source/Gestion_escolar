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