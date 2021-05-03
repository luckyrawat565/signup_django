from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm as user_signup
from .forms import usersignup
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'src/home.html')



def user_signup(request):
    if request.method == "POST":
        form = usersignup(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request,'Your account has been created. You can login now !')
            return redirect('profile/')  
    else:
        form = usersignup()
    return render(request, 'src/signup.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('../profile')
        else:
            fm = AuthenticationForm()
        return render(request,'src/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('../profile/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../login')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'src/profile.html')
    else:
        return HttpResponseRedirect('../login')
    