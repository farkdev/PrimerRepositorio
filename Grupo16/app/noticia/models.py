from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.



class Categoría(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo =  models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoría, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticia', default='static/assets/img/default.png')
    publicado = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo

    def delete(self, using = None , keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()



    def get_absolute_url(self):
        return reverse("blog", args=(str(self.id)))

class Comentario(models.Model):
    comentarios = models.ForeignKey(Noticia, related_name="comentarios", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    texto = models.TextField(max_length=250)
    fecha = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return ("comentario en  {self.comentarios} {self.nombre} {self.texto}")