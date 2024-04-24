

from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    return render(request, "index.html" )


def trainer_view(request):
    return render(request, "trainer.html")

def contact_view(request):
    return render(request, "contact.html")

def why_view(request):
    return render(request, "why.html")


def base_view(request):
    return render(request,"base.html")
