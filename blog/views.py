from django.shortcuts import render
from django.http import *
from .models import entries



def show_one_entry(request, element_id):
    try:
        print [entries[int(element_id)]]
        return render(request, "blog.html" ,{"all_entries": [entries[int(element_id)]]})
    except IndexError:
        raise Http404("We don't have any.")



def show_entries(request):
    print entries
    return render(request, "blog.html", {"all_entries": entries, "size": range(len(entries))})
