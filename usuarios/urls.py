from django.contrib import admin
from django.urls import path, include
from .views import register
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("registro", register, name="registro"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("login", login, name="login"),
    
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  path('registro', RegistroUsuario.as_view(), name="registro"),