# Proyecto 10 - Gestión Escolar

Sistema backend desarrollado con Django Rest Framework para digitalizar y centralizar la gestión académica de un establecimiento educacional. 

**Desarrollador:** Jorge Faundez

## Características Implementadas

* **Base de Datos Centralizada:** Modelos relacionales para Docentes, Alumnos y Registros Académicos con historial automático de fechas.
* **Seguridad y Perfiles de Acceso:** 
  * Ocultamiento de código en producción (`DEBUG = False`).
  * Página 404 personalizada.
  * Acceso público de solo lectura para el listado de docentes.
  * Acceso privado (requiere autenticación) para la gestión de alumnos y registros.
* **Reglas de Negocio:** Validación estricta para calificaciones (solo permite valores entre 1.0 y 7.0).
* **Indicadores de Gestión:** Endpoint personalizado para la obtención de estadísticas en tiempo real (total de alumnos, docentes y promedio general).

## Instalación y Ejecución

Sigue estos pasos en la terminal para levantar el proyecto localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>