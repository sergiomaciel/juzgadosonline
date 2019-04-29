from django.db import models
from django.utils import timezone
from expedientes.models import Expediente,Actualizacion


class LogExpediente(models.Model):
   expediente = models.ForeignKey(Expediente, null=True, on_delete=models.CASCADE)
   fecha = models.DateTimeField(default=timezone.now, null=True)
   accion = models.CharField(max_length=50)

class LogActualizacion(models.Model):
   actualizacion = models.ForeignKey(Actualizacion, null=True, on_delete=models.CASCADE)
   fecha = models.DateTimeField(default=timezone.now, null=True)
   accion = models.CharField(max_length=50)