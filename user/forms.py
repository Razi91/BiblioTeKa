
from user.models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

class UserForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['first_name', 'last_name', 'email']

class ClientForm(ModelForm):
     class Meta:
         model = Client
         fields = ['birthday', 'pesel', 'credits']

# class RegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.CharField(max_length=75)
#
#     class Meta(UserCreationForm.Meta):
#         fields = ('username','first_name','last_name', 'email')