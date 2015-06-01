from books.models import *
from user.models import *
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
    book = BookTitle.data.get(id=int(id))
    if request.GET.get('action') == 'loan':
        pub = request.GET.get('pub')
        entities = BookEntity.objects.filter(book_id=pub, quality__gt=0, )
        entity = None
        for e in entities:
            if Loan.objects.filter(book=e, returned__isnull=True).count() == 0:
                entity = e
                break
        if entity is not None:
            loan = Loan(
                client=request.user.client,
                book=entity,
                date=datetime.now(),
                pricing=entity.book.pricing,
                subscription=None
            )
            loan.loan(request.user.client)
            loan.save()
            request.user.client.save()
    if request.GET.get('action') == 'reserve':
        pub = request.GET.get('pub', None)
        if pub is not None:
            entity = BookEdition.objects.filter(id=pub).first()
        else:
            entity = None
        reservation = Reservation(
            client=request.user.client,
            book=entity,
            title=book,
            date=datetime.now(),
            pricing=entity.pricing if entity is not None else None,
            subscription=None
        )
        reservation.save()
    dict = {
        'book': book
    }
    return render(request, "books/publications.html", dict)


def return_book(request):
    if request.method == 'post':
        uuids = request.POST.get('uuids').split('\n')
        left = []
        returned = []
        for uuid in uuids:
            db = Loan.objects.filter(book__uuid__startswith=uuid)
            if db.count() == 1:
                loan = db.first()
                loan.back(loan)
                returned.append(loan.book)
            else:
                left.append(uuid)
        dict = {
            'uuids': '\n'.join(left),
            'returned': returned
        }
        return render(request, "books/return.html", dict)
    dict = {
        'uuids': ''
    }
    return render(request, "books/return.html", dict)
