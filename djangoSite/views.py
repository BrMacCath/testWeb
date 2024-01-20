from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render,redirect

def index(request):
    return render(request, "index.html")

def contact(request):
    context={}
    return render(request, "contact.html",context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success('Account was created for ' + user)
            return redirect('login')

    context={'form':form,'request':request}
    return render(request,"accounts/register.html",context)

def loginPage(request):
    if request.method=="POST":
        username =request.POST.get("username")
        password =request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Username OR Password is incorrect.")
    context={}
    return render(request,"accounts/login.html")