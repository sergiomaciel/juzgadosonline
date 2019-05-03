import requests
from bs4 import BeautifulSoup


class BuscarDespachos():
   #despachos = Despacho.objects.filter(ultima_fecha__lte= timedelta(days=-1))   
   def __init__(self, url):
      self.despachos = []
      self.nombre_archivo = ""
      self.url_juzgado = ""      
      
      self.generarUrl(url)
      self.listar(url)

   #Con url demo genera la url de juzgado y el archivo
   def generarUrl(self, url):
      Vurl = url.split("/")
      nombre = Vurl.pop()
      self.url_juzgado = url.replace(nombre, "")
      self.nombre_archivo = nombre[:-14]
      return self.url_juzgado

   def listar(self, url):
      #Scanear url_juzgado y extraer los links
      res = requests.get(self.url_juzgado).text
      soup = BeautifulSoup(res)
      links = soup.find_all('a')
      
      for link in links:
         link = link.get('href')
         nom_fecha_exten = link.split("/").pop()
         nombre = nom_fecha_exten[:-14]
         fecha = nom_fecha_exten[len(nombre):-4]
         # Verifica que el link del archivo sea como el demo
         if (nombre == self.nombre_archivo):
            self.despachos.append(
                  {  'nombre':nom_fecha_exten,
                     'fecha':fecha,
                  }
               ) 
      return self.despachos

