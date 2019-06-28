from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse


class loginView(View):
   
   def post(self, request):
      form = AuthenticationForm(data=request.POST)
      username = request.POST.get('username')
      password = request.POST.get('password')
      if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(self.request, user)
                return HttpResponseRedirect('/juzgado/')
            else:
                print('User not found')
      else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'juzgado/usuario/login.html', {'msg':'Credenciales Incorrectas'})
       
   
   def get(self, request):
      return render(request, 'juzgado/usuario/login.html', {})
