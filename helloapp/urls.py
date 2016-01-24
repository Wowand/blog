from django.conf.urls import patterns,include,url
from django.contrib import admin
from django.views.generic import TemplateView
from collection.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^things/(?P<slug>[-\w]+)/$',
        things_details,
        name='things_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$',
        edit_thing,
        name='edit_thing'),
    url(r'^graph/$',
        TemplateView.as_view(template_name='graph.html')),
    url(r'^receipt/$', get_receipts, name='get_receipts'),
    url(r'^admin/', admin.site.urls),
]
