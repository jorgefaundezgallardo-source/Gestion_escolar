from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .serializers import DocenteSerializer, AlumnoSerializer, RegistroAcademicoSerializer
from .models import Docente, Alumno, RegistroAcademico

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all() 
    serializer_class = DocenteSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly] 

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all() 
    serializer_class = AlumnoSerializer 
    permission_classes = [IsAuthenticated] 

class RegistroAcademicoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcademico.objects.all() 
    serializer_class = RegistroAcademicoSerializer 
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

    # --- NUEVAS VISTAS WEB  ---
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# 1. Vista Pública de Bienvenida (Function Based View sin protección)
def vista_publica(request):
    return render(request, 'bienvenida.html')

# 2. Vista Protegida Basada en Función (FBV)
@login_required # 
def vista_protegida_funcion(request):
    contexto = {'tipo_vista': 'Function Based View (FBV)'}
    return render(request, 'protegida.html', contexto)

# 3. Vista Protegida Basada en Clase (CBV)
class VistaProtegidaClase(LoginRequiredMixin, TemplateView):
    # LoginRequiredMixin 
    template_name = 'protegida.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_vista'] = 'Class Based View (CBV)'
        return context