from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse("Mūsų naujas puslapis")

def categories(request, catid):
    return HttpResponse(f"<h1>Puslapių kategorijos</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)>2022:
        raise Http404()

def pageNotFound(request, exeption):
    return HttpResponseNotFound("<h1>PUSLAPIS NERASTAS</h1>")

