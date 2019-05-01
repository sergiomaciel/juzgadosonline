from django.db import models
from django.utils import timezone
from .plantilla import Plantilla
from juzgados.models import Juzgado


class Despacho(models.Model):
   juzgado = models.ForeignKey(Juzgado, null=True, on_delete=models.CASCADE)
   url = models.CharField(max_length=100, null=True)
   plantilla = models.ForeignKey(Plantilla, null=True, on_delete=models.CASCADE)
   activo = models.BooleanField(default=False,null=False)
   ultima_fecha = models.DateTimeField(blank=True, null=True)

   def __str__(self):
      return str(self.juzgado)+" - "+str(self.ultima_fecha)+" - "+str(self.activo)
