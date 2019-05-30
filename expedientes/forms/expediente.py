from django import forms
from django.contrib.auth.models import User
from juzgados.models import Juzgado, Ciudad, Provincia
from expedientes.models import Expediente

class SubsAgregarForm(forms.Form):

   provincia = forms.ModelChoiceField(queryset=None)
   ciudad = forms.ModelChoiceField(queryset=None)
   juzgado = forms.ModelChoiceField(queryset=Juzgado.objects.all())
   numero = forms.CharField(initial='000/00')

   def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['provincia'].queryset = Provincia.objects.all()
         self.fields['ciudad'].queryset = Ciudad.objects.all()
