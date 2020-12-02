from django.contrib import admin
from . import models


@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name'
    ]
    search_fields = [
        'id',
        'username',
        'email'
    ]

    list_filter = [
    ]