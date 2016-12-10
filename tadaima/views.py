from django.shortcuts import render
from django.http import *


def home(request):
    return render(request, "tadaima.html")


