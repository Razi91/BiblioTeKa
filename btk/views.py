__author__ = 'jkonieczny'

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html", {

    })