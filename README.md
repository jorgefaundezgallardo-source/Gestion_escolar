# Proyecto 10 - Gestión Escolar

Backend desarrollado en Django y Django Rest Framework para la digitalización y centralización de la gestión académica.

## Instalación y Ejecución

### 1. Crear y activar el ambiente virtual
```bash
python -m venv env
```
En PowerShell:
```bash
.\env\Scripts\activate
```

### 2. Instalar dependencias:
```bash
pip install django djangorestframework
```

### 3. Aplicar migraciones:
```bash
python manage.py migrate
```

### 4. Crear usuario administrador 
```bash
python manage.py createsuperuser
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver --insecure
```
*(Nota: Se utiliza el flag `--insecure` para forzar la carga de los archivos estáticos y los estilos, debido a que el proyecto cuenta con el parámetro `DEBUG = False` activado por seguridad).*

## Rutas de Prueba

* **Bienvenida:** http://127.0.0.1:8000/ (Página principal del proyecto con accesos dinámicos)
* **Error 404:** http://127.0.0.1:8000/ruta-no-existe/ (Pantalla de error personalizada y controlada)
* **Panel de Administración:** http://127.0.0.1:8000/admin/
* **API Docentes:** http://127.0.0.1:8000/api/docentes/ (Ruta de acceso público)
* **API Alumnos:** http://127.0.0.1:8000/api/alumnos/ (Requiere autenticación)
* **API Registros:** http://127.0.0.1:8000/api/registros/ (Requiere autenticación)
* **Indicadores:** http://127.0.0.1:8000/api/registros/indicadores/ (Requiere autenticación)