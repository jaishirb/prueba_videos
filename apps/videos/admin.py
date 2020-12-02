from django.contrib import admin
from . import models


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
    ]
    search_fields = [
        'id',
        'nombre'
    ]

    list_filter = [
    ]


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'categoria'
    ]
    search_fields = [
        'id',
        'titulo',
        'categoria'
    ]

    list_filter = [
    ]


@admin.register(models.Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'curso'
    ]
    search_fields = [
        'id',
        'usuario__email',
        'curso__titulo'
    ]

    list_filter = [
    ]


@admin.register(models.ProgresoVideo)
class ProgresoVideoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'minutos_reproduccion_diaria',
        'curso',
        'usuario',
        'dia',
        'inscripcion',
        'categoria'
    ]
    search_fields = [
        'id',
        'curso__titulo',
        'usuario__email',
        'categoria__nombre'
    ]

    list_filter = [
        'dia'
    ]