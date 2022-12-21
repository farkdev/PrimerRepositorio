from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia



def Index(request):
    return render(request, "index.html")

def nosotros(request):
    return render(request, "nosotros.html")


class NoticiaListView(ListView):
    model = Noticia 
    template_name = "listaNoticias.html"


class NoticiaDetallada(DetailView):
    model = Noticia
    template_name = "blog.html"

