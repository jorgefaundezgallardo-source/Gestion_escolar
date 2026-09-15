from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Docente(models.Model):
    # CharField limita los caracteres. unique=True evita RUTs repetidos.
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    # EmailField valida automáticamente que tenga formato de correo (con @)
    email = models.EmailField(max_length=100, null=True, blank=True)
    especialidad = models.CharField(max_length=100, default="General")
    # BooleanField es ideal para estados de Verdadero/Falso (Activo/Inactivo)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)
    curso = models.CharField(max_length=50, default="Sin asignar")
    estado_matricula = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class RegistroAcademico(models.Model):
    # ForeignKey crea la relación entre tablas. CASCADE borra las notas si se borra el alumno.
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="registros")
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name="registros")
    asignatura = models.CharField(max_length=100)
    # DecimalField limita los números. max_digits=3 y decimal_places=1 permite notas como "7.0" o "4.5"
    calificacion = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(7.0)]
    )
    # DateTimeField(auto_now_add=True) guarda la fecha y hora exacta automáticamente
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Registro Académico"
        verbose_name_plural = "Registros Académicos"
        constraints = [
            models.UniqueConstraint(fields=['alumno', 'asignatura'], name='unique_alumno_asignatura')
        ]

    def __str__(self):
        return f"{self.asignatura} - {self.alumno.nombre}"
