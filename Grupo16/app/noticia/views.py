from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Noticia
from django.shortcuts import redirect


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

class NuevaNoticia(CreateView):
    model = Noticia
    template_name = "add_post.html"
    fields = ['titulo', 'subtitulo', 'texto', 'categoria', 'imagen']


    def form_valid(self, form):
        form.save()

        return redirect("noticias")