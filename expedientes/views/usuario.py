from django.shortcuts import render
from expedientes.forms import AbogadoForm, UserForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class login(View):
   
   def post(self, request):
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)
      if user:
         if user.is_active:
            login(request, user)
            return HttpResponseRedirect('dashboard')
         else:
            return HttpResponse("Your account was inactive.")
      else:
            return render(request, 'adminlte/usuario/login.html', {'msg':'Credenciales Incorrectas'})
       
   
   def get(self, request):
      return render(request, 'adminlte/usuario/login.html', {})

class registro(View):
   
   def post(self, request):    
      user_form = UserForm(data=request.POST)
      perfil_form = AbogadoForm(request.POST)
      if user_form.is_valid() and perfil_form.is_valid():
         user = user_form.save()
         user.set_password(user.password)
         user.save()
         # perfil = perfil_form.save()
         # perfil = perfil_form.save(commit=False)
         # perfil.usuario = user
         # # perfil.avatar = request.ger.
         # # if 'avatar' in request.FILES:
         # #    print('found it')
         # #    perfil.avatar = request.FILES['avatar']
         # perfil.save()

         return HttpResponseRedirect('usuario/login/')
      else:
         user_form = UserForm()
         return render(request,'adminlte/usuario/register.html',{'user_form':user_form})


   def get(self, request):
      user_form = UserForm()
      perfil_form = AbogadoForm()
      return render(request,'adminlte/usuario/register.html',{})
      # return render(request,'adminlte/usuario/register.html',
      #                      {'user_form':user_form,
      #                      'perfil_form':perfil_form})      
