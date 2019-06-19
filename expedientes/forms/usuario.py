from django import forms
from django_select2.forms import Select2MultipleWidget, ModelSelect2Widget
from django.contrib.auth.models import User
from expedientes.models import Abogado


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class AbogadoForm(forms.ModelForm):
     class Meta():
         model = Abogado
         fields = ('avatar','nombre','apellido')