from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.models import User
from expedientes.models import Expediente,Actualizacion
from juzgados.models import Juzgado


class Cargar():

   def __init__(self, juzgado:Juzgado):
      self.__juzgado = juzgado
      self.__usuarioRoot = User.objects.get(pk=1) 

   
   def agregar(self, datoExp):
      expBuscado = self.__existeExpediente(datoExp['numero'])      
      if (expBuscado == None):
         expNuevo = self.__agregarExpediente(datoExp)
         actNueva = self.__agregarActualizacion(expNuevo, datoExp)
      else:
         actBuscada = self.__existeActualizacion(expBuscado, datoExp['fecha_publicado'])
         if (actBuscada == None):
            actNueva = self.__agregarActualizacion(expBuscado, datoExp)
         else:   
            print("EL EXPEDIENTE "+datoExp['numero']+" YA TIENE ESTA ACTUALIZACION")   

   def actualizarExpediente(self, datoExp):
      expediente = self.__existeExpediente(datoExp['numero'])
      if (expediente != None):
         try:
            expediente.actor = datoExp['actor']
            expediente.demandado = datoExp['demandado']
            expediente.causa = datoExp['causa']
            expediente.fecha_publicado = datoExp['fecha_publicado']
            expediente.save(update_fields=[
               'actor',
               'demandado',
               'causa',
               'fecha_publicado'
               ])  
         except IndentationError as e:
            print("Error al actualizar EL EXPEDIENTE "+datoExp['numero'])
            print("Error = "+e)


   def actualizarActualizacion(self, datoExp):
      expediente = self.__existeExpediente(datoExp['numero'])
      actualizacion = self.__existeActualizacion(expediente, datoExp['fecha_publicado'])
      if (actBuscada != None):
         try:
            actualizacion.contenido = datoExp['contenido']
            actualizacion.fecha_publicado = datoExp['fecha_publicado']
            actualizacion.save(update_fields=[
               'contenido',
               'fecha_publicado'
               ])  
         except IndentationError as e:
            print("Error al actualizar la ACTUALIZACION "+datoExp['numero'])
            print("Error = "+e)

   #Verifica si exite el expediente
   def __existeExpediente(self, numero_expediente):      
      try:
         res = Expediente.objects.get(
            juzgado__exact = self.__juzgado, 
            numero__exact = numero_expediente
            )   
      except ObjectDoesNotExist:
         res = None      
      return res

      #Verifica si exite el expediente
   def __existeActualizacion(self, expediente:Expediente, fecha_publicado):      
      try:
         res = Actualizacion.objects.get(
            expediente__exact = expediente,
            fecha_publicado__exact = fecha_publicado
            )         
      except ObjectDoesNotExist:
         res = None      
      return res   


   def __agregarActualizacion(self, expediente:Expediente, datoExp):      
      A = Actualizacion(
         expediente=expediente,
         contenido=datoExp['contenido'],
         fecha_publicado=datoExp['fecha_publicado'],
         autor=self.__usuarioRoot
      )
      try:
         A.save()
      except IntegrityError:
         print("SE INTENTO AGREGAR LA ACTUALIZACION")
      
      return A

   def __actualizarActualizacion(self, expediente:Expediente, datoExp):      
      A = Actualizacion(
         expediente=expediente,
         contenido=datoExp['contenido'],
         fecha_publicado=datoExp['fecha_publicado'],
         autor=self.__usuarioRoot
      )
      try:
         A.save(update_fields=['name'])
      except IntegrityError:
        pass

      return A

   def __agregarExpediente(self, datoExp):
      E = Expediente(
         juzgado=self.__juzgado,
         numero=datoExp['numero'],
         actor=datoExp['actor'],
         demandado=datoExp['demandado'],
         causa=datoExp['causa'],
         fecha_publicado=datoExp['fecha_publicado'],
         autor=self.__usuarioRoot
         )
      E.save()   
      return E
     
         