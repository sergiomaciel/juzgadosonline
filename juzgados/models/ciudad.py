from django.db import models
from django.utils import timezone
from .provincia import Provincia


class Ciudad(models.Model):
   nombre = models.CharField(max_length=50)
   provincia = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)
      
   def __str__(self):
      return self.nombre
