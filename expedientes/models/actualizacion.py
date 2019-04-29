from django.db import models
from django.utils import timezone
from .expediente import Expediente


class Actualizacion(models.Model):
   expediente = models.ForeignKey(Expediente, null=True, on_delete=models.CASCADE)
   contenido = models.TextField( null=True)
   fecha_creado = models.DateTimeField(default=timezone.now)
   fecha_publicado = models.DateTimeField(blank=True, null=True)
   autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

   def publicar(self):
      self.fecha_publicado = timezone.now()
      self.save()

   def __str__(self):
      return str(self.expediente)+" --- "+str(self.contenido)[0:35]+" - "+ str(self.autor) +" - "+ str(self.fecha_creado)
   