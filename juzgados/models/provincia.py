from django.db import models
from django.utils import timezone


class Provincia(models.Model):
   nombre = models.CharField(max_length=35)

   def __str__(self):
      return self.nombre