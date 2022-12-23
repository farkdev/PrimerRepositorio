from . import views
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns =[
    path('', Index, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('noticias', NoticiaListView.as_view(), name="noticias") ,
    path('blog/<int:pk>', NoticiaDetallada.as_view(), name="blog"),
    path('add_post/', NuevaNoticia.as_view(), name="nuevaNoticia"),
    path('capacitaciones', capacitaciones, name="capacitaciones"),
    path('charlas', charlas, name="charlas"),
    path('seminarios', seminarios, name="seminarios"),
    path('cursos', cursos, name="cursos"),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
