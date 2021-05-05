from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class usersignup(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'conform Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name',]
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control'}),
                    'email':forms.EmailInput(attrs = {'class':'form-control'}),
                    'first_name':forms.TextInput(attrs = {'class':'form-control'}),                        
                    'last_name':forms.TextInput(attrs = {'class':'form-control'}),

        }
 

class userlogin(AuthenticationForm):
    username = forms.CharField(label = 'username',widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))

        
class EditUserForm(UserChangeForm):
        password = None
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email','date_joined','last_login']
            labels = {'email':'Email'}


class EditAdminProfile(UserCreationForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'  
        labels = {'email':'Email'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','desc']
        labels = {'title':'Title', 'desc':'Description'}
        widgets = {'title':forms.TextInput(attrs = {'class':'form-control'}),
        'desc':forms.Textarea(attrs = {'class':'form-control'})}

