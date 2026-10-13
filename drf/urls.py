"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de la API REST (Django REST Framework)
    path('api/', include('api.urls')), 
    
    # Sistema de Autenticación de Django (Login / Logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Nuevas Vistas Web 
    path('', views.vista_publica, name='vista_publica'), # URL base /
    path('protegida/funcion/', views.vista_protegida_funcion, name='vista_protegida_funcion'),
    path('protegida/clase/', views.VistaProtegidaClase.as_view(), name='vista_protegida_clase'),
]