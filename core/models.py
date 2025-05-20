from django.db import models

# Create your models here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email  = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Libro(models.Model):
    titulo     = models.CharField(max_length=200)
    autor      = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria  = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    publicado  = models.DateField()

    def __str__(self):
        return self.titulo
