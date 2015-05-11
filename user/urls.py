__author__ = 'jkonieczny'

from django.conf.urls import patterns, url

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from btk.privileges import *
from user.views import *

urlpatterns = patterns('',
    url(r'new-client^$',
        (new_client), name="NewClient"),
    # url(r'^at/([0-9:_\-]+)$',
    #     is_coordinator_or_superuser(views.shift_map), name='AtTime'),

)