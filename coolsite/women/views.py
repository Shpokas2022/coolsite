from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

menu = ["Apie svetainę", "Pridėti straipsnį", "Komentarai", "Įeiti"]
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu':menu, 'title':'PIRMIEJI METAI'})

def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title': 'Antrasis puslapis'})

def categories(request, catid):
    return HttpResponse(f"<h1>Puslapių kategorijos</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)>2022:
        raise Http404()

def pageNotFound(request, exeption):
    return HttpResponseNotFound("<h1>PUSLAPIS NERASTAS</h1>")

