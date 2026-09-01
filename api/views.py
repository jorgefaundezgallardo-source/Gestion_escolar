from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .serializer import DocenteSerializer, AlumnoSerializer, RegistroAcademicoSerializer
from .models import Docente, Alumno, RegistroAcademico

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all() #[cite: 2]
    serializer_class = DocenteSerializer #[cite: 2]
    permission_classes = [IsAuthenticatedOrReadOnly] 

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all() #[cite: 2]
    serializer_class = AlumnoSerializer #[cite: 2]
    permission_classes = [IsAuthenticated] 

class RegistroAcademicoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcademico.objects.all() #[cite: 2]
    serializer_class = RegistroAcademicoSerializer #[cite: 2]
    permission_classes = [IsAuthenticated] 

    # Endpoint personalizado para Indicadores de Gestión
    @action(detail=False, methods=['get'])
    def indicadores(self, request):
        total_alumnos = Alumno.objects.count()
        total_docentes = Docente.objects.count()
        promedio_notas = RegistroAcademico.objects.aggregate(Avg('calificacion'))['calificacion__avg']

        return Response({
            "total_alumnos": total_alumnos,
            "total_docentes": total_docentes,
            "promedio_general_escuela": round(promedio_notas, 1) if promedio_notas else 0.0
        })