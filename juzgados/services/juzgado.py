from juzgados.models import Juzgado
from expedientes.models import Expediente

class juzgadoService():

   def get(self, id):
      return Juzgado.objects.get(pk=id)


   def getExpediente(self,idJuzgado, numero):
      return Expediente.objects.filter(
         juzgado__id=idJuzgado,
         numero__contains=numero,
         fecha_publicado__isnull=False
         )


   def getAll(self):
      return Juzgado.objects.all()


   def TotalExpedientes(self):
      pass

   def UltimaActualizacion(self):
      pass   
