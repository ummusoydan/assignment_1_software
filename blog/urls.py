from django.conf.urls import url

from .views import show_entries, show_one_entry


urlpatterns = [
    url(r'^entries/$', show_entries),
    url(r'^entries/(?P<element_id>[0-9]+$)', show_one_entry),
    url(r'^$', show_entries),
]