from django.db import models
from django.utils import timezone
from .ciudad import Ciudad


class Juzgado(models.Model):
   nombre = models.CharField(max_length=50)
   ciudad = models.ForeignKey(Ciudad, null=True, on_delete=models.CASCADE)
  
   def __str__(self):
      return self.nombre