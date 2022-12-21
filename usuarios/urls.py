from django.contrib import admin
from django.urls import path, include
from .views import RegistroUsuario
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *



urlpatterns = [
    path('registro', RegistroUsuario.as_view(), name="registro"),
    path('', Index, name='inicio'),
    path('login', login,)
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

