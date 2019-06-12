import sys
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from expedientes.models import Expediente
from expedientes.services import actualizacionesService
from juzgados.services import juzgadoService

class expedienteService():
   pass

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