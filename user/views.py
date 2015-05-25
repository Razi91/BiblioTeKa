from books.models import *
from user.models import *
from user.forms import *

__author__ = 'jkonieczny'
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError

def new_client(request):
    user_form = UserForm(prefix='user_')
    client_form = ClientForm(prefix='client_')
    dict = {
        'forms': {
            'user': user_form,
            'client_form': client_form
        }
    }
    return render(request, "user/new-client.html", dict)