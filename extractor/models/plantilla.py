from django.db import models
'''
TIPOS = (
        ('conFoja', "Expte. N°: xxx/x -Foja: xx- {Actor} C/ {Demandado} S/{Causa} -"),
        ('sinFoja', "Expte. N°: xxx/x-SCA XXX C/ XXX S/XXXX - or Expte. N°: xxx/x XXX C/ XXX S/XXXX -"),
        ('L', 'Large'),
    )
'''    
class TipoCaratula(models.Model):
   nombre = models.CharField(max_length=50, null=True)
   codigo = models.CharField(max_length=30, unique=True)   
   caratula = models.CharField(max_length=150, null=False)
   numero = models.CharField(max_length=20, null=False)
   actor = models.CharField(max_length=100, null=True)
   demandado = models.CharField(max_length=100, null=True)
   causa = models.CharField(max_length=200, null=True)
   nota = models.TextField(max_length=150, null=True)

   def __str__(self):
      return self.nombre +" - "+self.codigo


class Plantilla(models.Model):   
   nombre = models.CharField(max_length=50, null=False)
   tipos_de_caratulas = models.ManyToManyField(TipoCaratula, related_name = 'tipos_de_caratulas')
   encabezado = models.TextField(null=True)
   separador =  models.CharField(max_length=100, null=True)
   demo = models.TextField(null=True)
   nota = models.TextField(max_length=150,null=True)

   def __str__(self):
      return self.nombre