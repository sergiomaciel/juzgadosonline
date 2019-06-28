from django import forms

from expedientes.models import Expediente

class actualizacionForm(forms.Form):

   TIPOS = (
      ('M', 'Movimiento'),
      ('P', 'Proveído/Actuación'),
      ('E', 'Escritos/Cargos'),
   )

   tipo = forms.ChoiceField(widget=forms.RadioSelect, choices=TIPOS)
   contenido = forms.CharField(widget=forms.Textarea)
