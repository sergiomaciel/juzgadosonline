from django.db import models

    
class TipoCaratula(models.Model):
   patron = models.CharField(max_length=250, unique=True)
   numero = models.CharField(max_length=20, null=False)
   actor = models.CharField(max_length=100, null=True)
   demandado = models.CharField(max_length=100, null=True)
   causa = models.CharField(max_length=200, null=True)
   nota = models.TextField(max_length=150, null=True)

   def __str__(self):
      return self.patron


class Plantilla(models.Model):   
   nombre = models.CharField(max_length=50, null=False)
   tipos_de_caratulas = models.ForeignKey(TipoCaratula, null=True, on_delete=models.CASCADE)
   encabezado = models.TextField(null=True)
   separador =  models.CharField(max_length=100, null=True)
   demo = models.TextField(null=True)
   nota = models.TextField(max_length=150,null=False)

   def __str__(self):
      return self.nombre