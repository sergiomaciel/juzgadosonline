import requests

class ExtraerExpedientes():
   
   def __init__(self):
      self.contenido = []
   
   # Sustrae el contenido del despacho
   # Quieta el encabezado
   # Clasifica el contenido en expedientes(limpiando el primero)
   def procesarDespacho(self, url, encabezado, separador):
      texto = requests.get(url).text[len(encabezado):]
      self.contenido = texto.split(separador)
      primero = self.contenido.pop(0)
      primero_limpio = primero.replace("--","")
      
      if (primero_limpio[0] == "-"):
         primero_limpio = primero_limpio[2:]
      
      self.contenido.insert(0,primero_limpio)
      return self.contenido

   def procesarExpediente(self):
      for expediente in self.contenido:
         pass

      pass
