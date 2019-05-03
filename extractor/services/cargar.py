from django.core.exceptions import ObjectDoesNotExist
from expedientes.models import Expediente,Actualizacion


class Cargar(): 
  
   #Verifica si exite el expediente
   def existeExpediente(juzgado, numero_expediente):      
      try:
         res = Expediente.objects.get(juzgado__exact=juzgado, numero__exact=numero_expediente)
         existe = True
      except ObjectDoesNotExist:
         existe = False 
      
      return existe


   def Actualizacion(self):
      A = Actualizacion()
      A.save()
      pass


   def Expediente(self):
      E = Expediente("nom", ajsahda)
      E.save()
      E.publicar()   
      pass
     
         