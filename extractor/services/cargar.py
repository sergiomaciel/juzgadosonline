from django.core.exceptions import ObjectDoesNotExist
from expedientes.models import Expediente,Actualizacion
from juzgados.models import Juzgado


class Cargar():

   def __init__(self, juzgado:Juzgado, **kwargs):

      if self.__existeExpediente(juzgado, kwargs['numero']):
         self.__agregarExpediente(juzgado, kwargs)
      else:
         pass


   
   #Verifica si exite el expediente
   def __existeExpediente(self, juzgado, numero_expediente):      
      try:
         res = Expediente.objects.get(juzgado__exact=juzgado, numero__exact=numero_expediente)
         existe = True
      except ObjectDoesNotExist:
         existe = False
      
      return existe

      #Verifica si exite el expediente
   def __existeActualizacion(self, expediente, fecha_creado):      
      try:
         res = Actualizacion.objects.get(expediente__exact=expediente, fecha_creado__exact=fecha_creado)
         existe = True
      except ObjectDoesNotExist:
         existe = False
      
      return existe   


   def __agregarActualizacion(self, **kwargs):
      A = Actualizacion(
         kwargs['expediente'],
         kwargs['contenido'],
         kwargs['fecha_creado'],
         kwargs['fecha_publicado'],
         kwargs['autor'],
      )
      A.save()
      pass


   def __agregarExpediente(self, juzgado:Juzgado, **kwargs):
      E = Expediente(
         Juzgado,
         kwargs['numero'],
         kwargs['actor'],
         kwargs['demandado'],
         kwargs['causa'],
         kwargs['fecha_creado'],
         kwargs['fecha_publicado'],
         )
      E.save()   
      pass
     
         