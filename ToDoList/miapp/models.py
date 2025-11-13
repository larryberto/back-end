from django.db import models

# Create your models here.
class Tarea(models.Model):
    tarea = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    
def __str__(self):
    return self.tarea
