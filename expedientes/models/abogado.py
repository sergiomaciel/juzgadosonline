from django.db import models
from datetime import datetime
from .expediente import Expediente
from django.contrib.auth.models import User


class Abogado(models.Model):
   usuario = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatar_user',blank=True)
   nombre = models.CharField(max_length=100, null=True)
   apellido = models.CharField(max_length=100, null=True)
   creado = models.DateField(default=datetime.now().day)
