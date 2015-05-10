from django.conf.urls import patterns, include, url

from django.contrib import admin
from btk.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'btk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^manage/', include('manage.urls', "map")),
    url(r'^books/', include('books.urls', "books")),
    #url(r'^user/', include('user.urls', "user")),

    url(r'^', index),
)
