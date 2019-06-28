from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from expedientes.models import Expediente, Actualizacion

class actualizacionService():
   
   def __init__(self, usuario:User, expediente:Expediente):
      self.__expediente = expediente
      self.__usuario = usuario
      self.msg = ''    
   

   def agregar(self,contenido, tipo, publicado=datetime.now()):      
      A = Actualizacion(
         expediente=self.__expediente,
         tipo=tipo,
         contenido=contenido,
         fecha_publicado=publicado,
         autor=self.__usuario
      )
      try:
         A.save()
      except IntegrityError:
         self.msg = "ERROR AL AGREGAR LA ACTUALIZACION"
      
      return A

   def actualizar(self, id, contenido, tipo, publicado=datetime.now()):
      actualizacion = Actualizacion.objects.get(pk=id)
      actualizacion.contenido = contenido
      actualizacion.tipo = tipo
      actualizacion.fecha_publicado = publicado
      try:
         actualizacion.save(update_fields=['tipo','contenido','fecha_publicado'])
      except IntegrityError:
        self.msg = "ERROR AL ACTUALIZAR"

      return actualizacion

      

class actualizacionesService():

   def __init__(self, idExpediente):
      self.actualizaciones = Actualizacion.objects.filter(expediente=idExpediente).order_by('-fecha_publicado')
      self.fechas = [A.fecha_publicado.strftime('%Y-%m-%d') for A in self.actualizaciones] 
      try:
         self.ultima = datetime.strptime(self.fechas[0], "%Y-%m-%d")
      except IndexError:
         self.ultima = ''


   def caducidad(self, dias):
      if (self.ultima != ''):
         caducidad = {
            'fecha':self.ultima + timedelta(days=dias),
            'falta': ((self.ultima+ timedelta(days=dias)) - datetime.now()).days
         }  
      return caducidad   