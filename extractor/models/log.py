from django.db import models
from django.utils import timezone
from expedientes.models import Expediente,Actualizacion
from .despacho import Despacho


class LogExpediente(models.Model):
   expediente = models.ForeignKey(Expediente, null=True, on_delete=models.CASCADE)
   fecha = models.DateTimeField(default=timezone.now, null=True)
   accion = models.CharField(max_length=50)
   despacho = models.ForeignKey(Despacho, null=True, on_delete=models.CASCADE)

   def __str__(self):
      return str(self.despacho)+" - "+str(self.expediente)+" - "+str(self.fecha)

class LogActualizacion(models.Model):
   actualizacion = models.ForeignKey(Actualizacion, null=True, on_delete=models.CASCADE)
   fecha = models.DateTimeField(default=timezone.now, null=True)
   accion = models.CharField(max_length=50)
   despacho = models.ForeignKey(Despacho, null=True, on_delete=models.CASCADE)

   def __str__(self):
      return str(self.despacho)+" - "+str(self.actualizacion)+" - "+str(self.fecha)