from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NuevoUsuario
from django.contrib.auth import login , authenticate
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = NuevoUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            messages.succes(request, f'usuario {username} creado')
            return redirect('inicio')

    else:
        form = NuevoUsuario()
        
    context = {'form' : form}
    return render(request, "registro.html", context)




# class RegistroUsuario(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/registro.html'
#     success_url = reverse_lazy('usuarios:login')
    


def Index(request):
    return render(request, "index.html")




def login(request) :
    template_name = "registration/registro.html"
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)

        if user is not None:
            login(request, user)
            return render(request, "index.html", {"mensaje":f"Bienvenido{usuario}"})


    return render(request, "login.html")





























# def login_request(request):
#     if request.method =="POST":

#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             usuario = form.cleaned_data.get("username")
#             contra = form.cleaned_data.get("password")

#             user = authenticate(username=usuario, password=contra)

#             if user is not None:
#                 login(request, user)
#                 return render(request, "index.html", {"mensaje":f"Bienvenido{usuario}"})
                
#             else:
#                 return HttpResponse(f"Usuario incorrecto")

#         else: 
#             return HttpResponse(f"Incorrecto {form}")    
    

#     form = AuthenticationForm()
    
#     return render(request, "login.html")