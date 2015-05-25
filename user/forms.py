
from user.models import *

from django.forms import ModelForm

class UserForm(ModelForm):
     class Meta:
         model = User
         fields = []

class ClientForm(ModelForm):
     class Meta:
         model = Client
         fields = ['birthday', 'pesel', 'credits']
