from datetime import datetime, timedelta
from expedientes.models import Actualizacion

class actualizacionSercice():
   pass

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