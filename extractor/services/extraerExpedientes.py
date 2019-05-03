import requests, re
from extractor.models import Despacho

class ExtraerExpedientes():
   
   def __init__(self):
      self.despacho = Despacho.objects.get(pk=1)
      self.contenido = []
      self.expedientes = []     
   
   # Sustrae el self.contenido del despacho
   # Quieta el encabezado
   # Clasifica el self.contenido en expedientes(limpiando el primero)
   def procesarDespacho(self, url):
      texto = requests.get(url).text[len(self.despacho.plantilla.encabezado):]
      self.contenido = texto.split(self.despacho.plantilla.separador)
      primero = self.contenido.pop(0)
      primero_limpio = primero.replace("--","")
      
      if (primero_limpio[0] == "-"):
         primero_limpio = primero_limpio[2:]
      
      self.contenido.insert(0,primero_limpio)
      return self.contenido

   #Quita las partes de la CADENA y retorna una cadena limpia
   def restoCaratula(self, cadena, partes):
      resto = []
      for parte in partes:
         patron = re.compile(parte)
         tupla = patron.subn("<>", cadena)
         cadena = tupla[0].strip()
      
      resto = cadena.split("<>")
      while "" in resto: resto.remove("")   
      return resto 

      
   # Genera el resto_base de las caratulas
   # Quita de la caratula el resto_base
   # Guarda el contenido y las partes del expediente
   def procesarExpediente(self):      
      tipoCaratula = self.despacho.plantilla.tipos_de_caratulas
      patronBase = tipoCaratula.patron
      partesBase = [
         tipoCaratula.numero,
         tipoCaratula.actor,
         tipoCaratula.demandado,
         tipoCaratula.causa,
         ]
      restoBase = self.restoCaratula(patronBase, partesBase)
      
      for expediente in self.contenido:
         partesExpediente = self.restoCaratula(expediente, restoBase)
         if (len(partesExpediente)>3):
            self.expedientes.append(
               {
                  'numero':partesExpediente[0],
                  'actor':partesExpediente[1],
                  'demandado':partesExpediente[2],
                  'causa':partesExpediente[3],
                  'contenido':expediente
               }
            )
         else:
            self.expedientes.append(
               {
                  'numero':partesExpediente[0],
                  'actor':partesExpediente[1],
                  'demandado':'',
                  'causa':partesExpediente[2],
                  'contenido':expediente
               }
            )

      return self.expedientes
