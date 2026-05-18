from django.db import models

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    genero_principal = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    bandas_donde_participo = models.TextField()
    genero_principal = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.IntegerField() 

    def __str__(self):
        return self.titulo

