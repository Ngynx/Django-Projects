from django.db import models

class Pregunta(models.Model):
   def __str__(self):
       return self.pregunta_texto

class Alternativa(models.Model):
   def __str__(self):
       return self.alternativa_texto
