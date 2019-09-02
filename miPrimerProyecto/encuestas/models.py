import datetime


from django.db import models
from django.utils import timezone


class Pregunta(models.Model):
     pregunta_texto = models.CharField(max_length=200)
     fecha_pub = models.DateTimeField('fecha de publicacion')
     def __str__(self):
         return self.pregunta_texto


class Alternativa(models.Model):
     pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
     alternativa_texto = models.CharField(max_length=200)
     votos = models.IntegerField(default=0)
     def __str__(self):
         return self.alternativa_texto
