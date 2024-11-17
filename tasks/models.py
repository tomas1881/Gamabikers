from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(null=True)
    imprtante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.titulo + '- by ' + self.usuario.username



class Post(models.Model):
    Nombre_vendedor = models.CharField(max_length=255)
    marca = models.CharField(max_length=255, default="Título")
    año = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='foto/', default='imagen')
    
    def __str__(self):
       return f"{self.marca} - {self.Nombre_vendedor}"
