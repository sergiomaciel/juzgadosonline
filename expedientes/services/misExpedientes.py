import sys
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from datetime import datetime
from expedientes.models import Expediente, Actualizacion
from juzgados.services import juzgadoService

class MisExpediente():

   def __init__(self, user:User):
      self.user = user
      self.suscripciones = []
      self.autor = Expediente.objects.filter(autor=self.user)
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

   
   def preCargaCrear(self, idJuzgado, numero):
      juzgado = juzgadoService()
      E = Expediente(
         juzgado=juzgado.get(idJuzgado),
         numero=numero,
         actor='',
         demandado='',
         causa='',
         autor=self.user
         )
      E.save()
      E.subscriptores.add(self.user)


   def preCargaActualizar(self, idExpediente, idJuzgado, numero):
      try:
         juzgado = juzgadoService()         
         E = Expediente.objects.get(pk=idExpediente)

         E.juzgado = juzgado.get(idJuzgado)
         E.numero = numero
         E.save(update_fields=[
               'juzgado',
               'numero'
               ])
      except ObjectDoesNotExist:
         pass


   def creados(self):
      return self.autor


   def getExpediente(self,idExpediente):
      res = ' '
      for expediente in self.autor:
         if (expediente.id == idExpediente):
            return expediente
      
      return res

