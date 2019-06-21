import sys
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from expedientes.models import Expediente
from expedientes.services import actualizacionesService, actualizacionService
from juzgados.models import Juzgado
from juzgados.services import juzgadoService

class expedienteService():
   
   def __init__(self, usuario:User, juzgado:Juzgado):
      self.__juzgado = juzgado
      self.__usuario = usuario
      self.msg = ''

   
   def agregar(self, numero,actor='',demandado='',causa=''):
      expBuscado = self.__existeExpediente(numero)      
      if (expBuscado == None):
         self.__agregarExpediente(numero, actor, demandado, causa)
      else:
         self.msg = "EL EXPEDIENTE "+numero+" YA EXISTE"   

   #Verifica si exite el expediente
   def __existeExpediente(self, numero):      
      try:
         res = Expediente.objects.get(
            juzgado__exact = self.__juzgado, 
            numero__exact = numero
            )   
      except ObjectDoesNotExist:
         res = None      
      return res

   def __agregarExpediente(self, numero, actor, demandado, causa):
      E = Expediente(
         juzgado=self.__juzgado,
         numero=numero,
         actor=actor,
         demandado=demandado,
         causa=causa,
         fecha_publicado=datetime.now(),
         autor=self.__usuario
         )
      E.save()
      #Agrega al Expediente el primer movimiento
      A = actualizacionService(self.__usuario, E)
      A.agregar("Creado", "M")
      return E

   def actualizar(self, numero,actor='',demandado='',causa=''):
      expediente = self.__existeExpediente(numero)
      if (expediente != None):
         try:
            expediente.actor = actor
            expediente.demandado = demandado
            expediente.causa = causa
            expediente.fecha_publicado = datetime.now()
            expediente.save(update_fields=[
               'actor',
               'demandado',
               'causa',
               'fecha_publicado'
               ])  
         except IndentationError as e:
            self.msg = "Error al actualizar EL EXPEDIENTE "+numero + " Error = "+e
            print(self.msg)
      return expediente      


class expedienteDatoService():

   def __init__(self, user:User, idExp):
      self.user = user
      self.expediente = Expediente.objects.get(pk=idExp)
      A = actualizacionesService(idExp)
      self.actualizaciones = A.actualizaciones
      self.fechas = A.fechas
      self.ultimaActualizacion = A.ultima
      self.caducidadad = {
         '30':A.caducidad(30),
         '60':A.caducidad(60),
         '90':A.caducidad(90)
      }
      if (self.user in self.expediente.subscriptores.all()):
         self.subcripto = True
      else:
         self.subcripto = False


   def suscripcion(self):
      if (self.user in self.expediente.subscriptores.all()):
         self.expediente.subscriptores.remove(self.user)
         self.subcripto = False
      else:
         self.expediente.subscriptores.add(self.user)
         self.subcripto = True 
      
      pass    