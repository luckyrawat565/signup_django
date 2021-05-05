
#from django.contrib.auth.forms import UserCreationForm as user_signup
#from django.contrib.auth.forms import AuthenticationForm, UserChangeForm,
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User ,Group
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . forms import userlogin, EditAdminProfile,usersignup,EditUserForm, PostForm
from .models import Blog


def index(request):     
    posts = Blog.objects.all()
    return render(request, 'src/home.html',{'posts':posts})

def user_signup(request):
    if request.method == "POST":
        forms = usersignup(request.POST)
        if forms.is_valid():

            user = forms.save()
            group = Group.objects.get(name = 'author')
            user.groups.add(group)

            messages.success(request,'Your account has been created. You can login now !')
            return redirect('../dashboard/')  
    else:
        forms = usersignup()
    return render(request, 'src/signup.html',{'form':forms})



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = userlogin(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('../dashboard')
        else:
            fm = userlogin()
        return render(request,'src/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('../dashboard/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../login')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance = request.user)
            else:
                fm  = EditUserForm(request.POST, instance = request.user)

            if fm.is_valid():
                messages.success(request, 'profile update sucessfully')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance = request.user)
            else:
                fm = EditUserForm(instance = request.user)
        return render(request, 'src/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('../login')
    

def user_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            posts = Blog.objects.all()
        else:
            posts = Blog.objects.filter(user = request.user)
        return render(request, 'src/dashboard.html',{'name':request.user.username,'posts':posts})
        
    else:
        return HttpResponseRedirect('../login')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                uname = request.user
                pst = Blog(title = title, desc = desc, user = uname)
                pst.save()
                messages.success(request, 'updated sucessfully!!')
        else:
            form = PostForm()
    return render(request,'src/addpost.html',{'form':form})

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blog.objects.get(pk = id)
            form = PostForm(request.POST, instance = pi)
            if form.is_valid():
                form.save()
        else:
            pi = Blog.objects.get(pk = id)    
            form = PostForm(instance = pi)
        return render(request,'src/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        pi = Blog.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/src/dashboard')
    else:
        return HttpResponseRedirect('/login/')
