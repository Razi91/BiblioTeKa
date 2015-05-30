from books.models import *

__author__ = 'jkonieczny'
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError

def titles(request):
    books = BookTitle.data.all()
    dict = {
        'books': books
    }
    return render(request, "books/titles.html", dict)
    
def title(request, id):
    books = BookTitle.data.filter(id=int(id)).first()
    dict = {
        'book': books
    }
    return render(request, "books/titles.html", dict)