from django.db import models

class Docente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    matriculado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class RegistroAcademico(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    asignatura = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('alumno', 'asignatura')

    def __str__(self):
        return f"{self.asignatura} - {self.alumno.nombre}"