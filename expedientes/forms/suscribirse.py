from django import forms
from django.contrib.auth.models import User
from expedientes.models import Expediente

class suscribirseForm(forms.Form):
    
   def save(self, IdUser, IdExp):
      expediente = Expediente.objects.get(pk=IdExp)
      usuario = User.objects.get(pk=IdUser)
      
      if (IdUser in expediente.subscriptores):
         expediente.subscriptores.remove(usuario)
      else:
         expediente.subscriptores.add(usuario)
      
      return expediente

        
