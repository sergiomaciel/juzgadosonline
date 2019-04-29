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
   autor = models.ForeignKey('auth.User', null=True,default=None, on_delete=models.SET_DEFAULT)

   subscriptores = models.ManyToManyField('auth.User',related_name = 'subscriptores', null=True)

   def publicar(self):
      self.fecha_publicado = timezone.now()
      self.save()
   
   def __str__(self):
      if ( (isinstance(self.demandado , (str))) ):
         caratula = self.numero +" - "+ self.actor +" C/ "+ self.demandado +" S/ "+ self.causa
      else:
         caratula = self.numero +" - "+ self.actor +" S/ "+ self.causa   
      return caratula
