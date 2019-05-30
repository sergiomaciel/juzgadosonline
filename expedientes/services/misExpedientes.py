import sys
from django.contrib.auth.models import User
from datetime import datetime
from expedientes.models import Expediente, Actualizacion

class MisExpediente():

   def __init__(self, user:User):
      self.user = user
      self.suscripciones = []
      expedientes = Expediente.objects.filter(subscriptores=self.user)
      for expediente in expedientes:
         try:
            actualizaciones = Actualizacion.objects.filter(expediente=expediente.pk).order_by('-fecha_publicado')
            ultimaAct = actualizaciones[0].fecha_publicado
            item = {
               'id':expediente.pk,
               'numero':expediente.numero,
               'juzgado':expediente.juzgado,
               'ultimaAct':ultimaAct,
               'DiasUltimaAct':(datetime.now() - datetime.strptime(ultimaAct.strftime('%Y-%m-%d'), "%Y-%m-%d")).days
            }
            self.suscripciones.append(item)
         except IndexError:
            pass

            
   def suscriptos(self):
      return self.suscripciones


   def novedades(self, hasta):
      novedades = []
      for expediente in self.suscripciones:
         if (  int(expediente.get('DiasUltimaAct')) <= int(hasta)):
            novedades.append(expediente)
      return novedades


   def creados(self):
      creados = Expediente.objects.filter(autor=self.user)
      return creados