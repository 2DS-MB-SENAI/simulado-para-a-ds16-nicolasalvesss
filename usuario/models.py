from django.db import models 
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    telefone = models.CharField(max_length=15)
    REQUIRED_FIELDS = ['telefone' ]

    def __str__(self):
        return self.telefone