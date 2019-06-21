from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from juzgados.models import Juzgado


class Delegado(models.Model):
   usuario = models.OneToOneField(User, on_delete=models.CASCADE)
   juzgado = models.ForeignKey(Juzgado, null=True, on_delete=models.CASCADE)
   creado = models.DateTimeField(default=datetime.now())

   def __str__(self):
      return str(self.usuario)+' - '+str(self.juzgado.nombre)
