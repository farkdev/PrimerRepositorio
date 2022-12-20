from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy




class RegistroUsuario(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('inicio')


def login(request):
    return render(request, "login.html")


def Index(request):
    return render(request, "index.html")