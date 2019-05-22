from django.db import models
from django.utils import timezone
from .expediente import Expediente


class Actualizacion(models.Model):
   expediente = models.ForeignKey(Expediente, null=True, on_delete=models.CASCADE)
   TIPOS = (
      ('M', 'Movimiento'),
      ('P', 'Proveído/Actuación'),
      ('E', 'Escritos/Cargos'),
   )
   tipo = models.CharField(null=True, default='M', max_length=1, choices=TIPOS)
   contenido = models.TextField(null=True)
   fecha_creado = models.DateTimeField(default=timezone.now)
   fecha_publicado = models.DateTimeField(blank=True, null=True)
   autor = models.ForeignKey('auth.User', default=None, on_delete=models.SET_DEFAULT)

   def publicar(self):
      self.fecha_publicado = timezone.now()
      self.save()

   def __str__(self):
      return str(self.expediente) +" - "+ str(self.tipo) +" - "+ str(self.fecha_creado)[0:19]
   