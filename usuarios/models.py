from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to="usuarios", default="static/assets/img/default.png")

    def get_absolute_url(self):
        return reverse("inicio")
