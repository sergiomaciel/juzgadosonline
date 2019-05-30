import sys
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from expedientes.models import Expediente, Actualizacion
from juzgados.services import juzgadoService

class expedienteService():

   def __init__(self, idUser):
      self.__user = User.objects.get(pk=idUser)
      # self.__user = user

   def crear(self, juzgado, numero):
      # self.autor = User.objects.get(pk=idAutor)
      self.juzgado = juzgadoService.get(nombre=juzgado)
      E = Expediente(
         juzgado=self.juzgado,
         numero=numero,
         actor='',
         demandado='',
         causa='',
         autor=self.__user
         )
      E.save()

   def get(self, idExp):
      
      self.expediente = Expediente.objects.get(pk=idExp,)
      self.actualizaciones = Actualizacion.objects.filter(expediente=idExp).order_by('-fecha_publicado')
      # self.ultimaActualizacion = self.actualizaciones[0].fecha_publicado.strftime('%Y-%m-%d')
      self.fechas = [A.fecha_publicado.strftime('%Y-%m-%d') for A in self.actualizaciones]
      
      try:
         self.ultimaActualizacion = datetime.strptime(self.fechas[0], "%Y-%m-%d")
         self.caducidadad = {
         '30':{
            'fecha':self.ultimaActualizacion + timedelta(days=30),
            'falta': ((self.ultimaActualizacion + timedelta(days=30)) - datetime.now()).days
         }, 
         '60':{
            'fecha':self.ultimaActualizacion + timedelta(days=60),
            'falta': ((self.ultimaActualizacion + timedelta(days=60)) - datetime.now()).days
         },
         '90':{
            'fecha':self.ultimaActualizacion + timedelta(days=90),
            'falta': ((self.ultimaActualizacion + timedelta(days=90)) - datetime.now()).days
         },
      }
      except IndexError:
         self.ultimaActualizacion = ''
         self.caducidadad = {}

      self.subcripto = False

      if (self.__user in self.expediente.subscriptores.all()):
         self.subcripto = True

      return {
         'expediente':self.expediente,
         'ultimaActualizacion':self.ultimaActualizacion,
         'suscripto':self.subcripto,
         'actualizaciones': self.actualizaciones,
         'fechas':self.fechas,
         'caducidadad':self.caducidadad
         }

   def suscripcion(self):
      if (self.__user in self.expediente.subscriptores.all()):
         self.expediente.subscriptores.remove(self.__user)
         self.subcripto = False
      else:
         self.expediente.subscriptores.add(self.__user)
         self.subcripto = True 
      
      return {
         'expediente':self.expediente,
         'ultimaActualizacion':self.ultimaActualizacion,
         'suscripto':self.subcripto,
         'actualizaciones': self.actualizaciones,
         'fechas':self.fechas,
         'caducidadad':self.caducidadad
         }        