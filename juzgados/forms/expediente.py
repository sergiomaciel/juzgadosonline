from django import forms

from expedientes.models import Actualizacion

class expedienteForm(forms.Form):

   numero = forms.CharField()
   actor = forms.CharField(required=False)
   demanadado = forms.CharField(required=False)
   causa = forms.CharField(required=False)

