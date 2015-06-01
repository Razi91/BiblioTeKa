__author__ = 'jkonieczny'

from django.conf.urls import patterns, url

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from btk.privileges import *
from books.views import *

urlpatterns = patterns('',
    #mapa
    url(r'^$',
        (titles), name="Browse"),
    url(r'title/([0-9]+)$',
        title, name="Title"),
    url(r'return/$',
        return_book, name="Return"),
    # url(r'^at/([0-9:_\-]+)$',
    #     is_coordinator_or_superuser(views.shift_map), name='AtTime'),

)