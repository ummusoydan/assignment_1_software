from django.shortcuts import render
from django.http import *
from .models import *
from .forms import BlogForm
from django.core.exceptions import PermissionDenied


def index(request):
    return HttpResponse('<h1>What you seek is not here.</h1></br><a href="entries">Entries Page</a>')


def list_all(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()


    return render(request, "blog.html", {"entries": Blog.objects.filter(user=request.user.id),
                                         "tags": Tag.objects.all()})


def list_one(request, item_id):
    try:
        entry = Blog.objects.get(id=item_id, user=request.user.id)
        return render(request, "detailed_blog.html", {"entry": entry})
    except Blog.DoesNotExist:
        raise Http404("We don't have what are you looking for.")


def redirect(request):
    return HttpResponse(r'<meta http-equiv="refresh" content="0; url=http://127.0.0.1:8000/blog/entries/" />')


def delete_all(request):
    Blog.objects.filter(user=request.user.id).delete()
    return HttpResponse(r'<meta http-equiv="refresh" content="0; url=http://127.0.0.1:8000/blog/entries/" />')
