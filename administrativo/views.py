from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
# Create your views here.


#def administrativo(request):

    #return render(request, "administrativo/administrativo.html")

def administrativo(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra, request=request)
            login(request, usuario)
            esadministrador=request.user.is_superuser
            if esadministrador:

                
                admin_url=reverse('admin:index')
                return redirect(admin_url)
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")

    form=AuthenticationForm()
    return render(request,"administrativo/administrativo.html",{"form":form})