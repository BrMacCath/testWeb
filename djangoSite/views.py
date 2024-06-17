from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import get_object_or_404, render,redirect
from .decorators import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")



def contact(request):
    context={}
    return render(request, "contact.html",context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')

        context={'form':form,'request':request}
        return render(request,"accounts/register.html",context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method=="POST":
            username =request.POST.get("username")
            password =request.POST.get("password")
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,"Username OR Password is incorrect.")
                return render(request,"accounts/login.html")
        context={}
        return render(request,"accounts/login.html",context)

@login_required(login_url='login')
def profilePage(request):
    return render(request,"accounts/profile.html")