from django.db import models
from django.utils import timezone
from juzgados.models import Juzgado

class ExepedienteManager(models.Manager):
   pass
class Expediente(models.Model):
   objects=ExepedienteManager()
   juzgado = models.ForeignKey(Juzgado, null=True, on_delete=models.CASCADE)
   numero = models.CharField(max_length=20, unique=True)   
   actor = models.CharField(max_length=100, null=True)
   demandado = models.CharField(max_length=100, null=True)
   causa = models.CharField(max_length=200, null=True)

   fecha_creado = models.DateTimeField(default=timezone.now, null=True)
   fecha_publicado = models.DateTimeField(blank=True, null=True)   
   autor = models.ForeignKey('auth.User', default=None, on_delete=models.SET_DEFAULT)

   subscriptores = models.ManyToManyField('auth.User', blank=True, related_name = 'subscriptores')

   def __str__(self):
      return self.numero+" - "+str(self.juzgado)

   '''
   def __str__(self):
      if ( (isinstance(self.demandado , (str))) ):
         caratula = self.numero +" - "+ self.actor +" C/ "+ self.demandado +" S/ "+ self.causa
      else:
         caratula = self.numero +" - "+ self.actor +" S/ "+ self.causa   
      return caratula
   '''   
