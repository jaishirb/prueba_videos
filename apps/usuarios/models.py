from django.contrib.auth.models import User
from django.db import models


class Usuario(User):
    pass

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
