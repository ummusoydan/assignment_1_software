from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^entries/delete', delete_all),
    url(r'^entries/(?P<item_id>[0-9]+)', list_one),
    url(r'^entries/$', list_all),
    url(r'^profile', redirect),
    url(r'^$', index),
]