from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import DocenteSerializer, AlumnoSerializer, RegistroAcademicoSerializer
from .models import Docente, Alumno, RegistroAcademico

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    # IsAuthenticatedOrReadOnly: Cualquiera puede ver a los docentes (público), 
    # pero solo usuarios autenticados pueden crear o editar.
    permission_classes = [IsAuthenticatedOrReadOnly] 

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    # IsAuthenticated: Información 100% privada. Requiere login obligatorio.
    permission_classes = [IsAuthenticated] 

class RegistroAcademicoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcademico.objects.all()
    serializer_class = RegistroAcademicoSerializer
    permission_classes = [IsAuthenticated]