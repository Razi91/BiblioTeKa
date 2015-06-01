from django.contrib.auth import authenticate, login, logout
from books.models import *
from user.models import *
from user.forms import *

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            pass
    else:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clients(request):
    dict = {
        'clients': Client.objects.all(),
        'subscriptions': Subscription.objects.all()
    }
    return render(request, "user/clients.html", dict)

def new_client(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        client_form = ClientForm(request.POST, prefix='client')
        dict = {
            'forms': {
                'user_form': user_form,
                'client_form': client_form,
            }
        }
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save(commit=False)
            user.username = "{0}.{1}".format(user.first_name.lower(), user.last_name.lower())
            password = User.objects.make_random_password()
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            dict = {
                'data': {
                    'user': user,
                    'client': client,
                }
            }
            return render(request, "user/new-client.html", dict)
        return render(request, "user/new-client.html", dict)
    user_form = UserForm(prefix='user')
    client_form = ClientForm(prefix='client')
    dict = {
        'forms': {
            'user_form': user_form,
            'client_form': client_form,
        }
    }
    return render(request, "user/new-client.html", dict)