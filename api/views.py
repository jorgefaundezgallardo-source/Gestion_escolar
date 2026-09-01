from rest_framework import viewsets
from .serializer import DocenteSerializer, AlumnoSerializer, RegistroAcademicoSerializer
from .models import Docente, Alumno, RegistroAcademico

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all() 
    serializer_class = DocenteSerializer 

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all() 
    serializer_class = AlumnoSerializer

class RegistroAcademicoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcademico.objects.all() 
    serializer_class = RegistroAcademicoSerializer 