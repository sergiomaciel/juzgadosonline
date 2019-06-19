from django.contrib.auth.models import User
from juzgados.models import Juzgado
from expedientes.models import Expediente

class juzgadoService():

   def buscarExpediente(self,idJuzgado, numero):
      return Expediente.objects.filter(
         juzgado__id=idJuzgado,
         numero__contains=numero,
         fecha_publicado__isnull=False
         )


   def getAllExpediente(self,idJuzgado):
      return Expediente.objects.filter(
         juzgado__id=idJuzgado,
         fecha_publicado__isnull=False
         )


   def getExpedienteAutor(self, idJuzgado, user:User):
      return Expediente.objects.filter(
         autor=user,
         juzgado__id=idJuzgado,
         fecha_publicado__isnull=False
         )


   def getJuzgado(self, id):
         return Juzgado.objects.get(pk=id)


   def getAllJuzgados(self):
      return Juzgado.objects.all()


   def TotalExpedientes(self):
      pass
