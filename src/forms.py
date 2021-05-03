from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class usersignup(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'conform Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email',]
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control'}),
                    'email':forms.EmailInput(attrs = {'class':'form-control'})                        
        }


class userlogin(AuthenticationForm):
    username = forms.CharField(label = 'username',widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))

        