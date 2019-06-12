from django.db import models
from django.utils import timezone
from juzgados.models import Juzgado


class Expediente(models.Model):
   juzgado = models.ForeignKey(Juzgado, null=True, on_delete=models.CASCADE)
   numero = models.CharField(max_length=20)   
   actor = models.CharField(max_length=100, null=True)
   demandado = models.CharField(max_length=100, default=None, blank=True)
   causa = models.CharField(max_length=200, null=True)

   fecha_creado = models.DateTimeField(default=timezone.now, null=True)
   fecha_publicado = models.DateTimeField(blank=True, null=True)   
   autor = models.ForeignKey('auth.User', default=None, on_delete=models.SET_DEFAULT)

   subscriptores = models.ManyToManyField('auth.User', blank=True, related_name = 'subscriptores')

   def __str__(self):
      caratula = self.numero
      
      if (self.actor != ''):
         caratula = caratula +" - "+ self.actor

      if ( self.demandado != ''):
         caratula = caratula +" C/ "+ self.demandado
      
      if ( self.causa != ''):
         caratula = caratula +" S/ "+ self.causa

      return caratula