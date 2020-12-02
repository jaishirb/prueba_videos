from django.db import models

from apps.utils.models import ModelBase
from apps.utils.shortcuts import get_object_or_none


class Categoria(ModelBase):
    nombre = models.CharField(
        max_length=120
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Curso(ModelBase):
    titulo = models.CharField(
        max_length=120
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Inscripcion(ModelBase):
    usuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'


class ProgresoVideo(ModelBase):
    minutos_reproduccion_diaria = models.FloatField(

    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )
    usuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE
    )
    dia = models.DateField(

    )
    inscripcion = models.ForeignKey(
        Inscripcion,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    categoria = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            inscripcion = get_object_or_none(
                Inscripcion,
                usuario=self.usuario,
                curso=self.curso
            )
            if inscripcion:
                self.inscripcion = inscripcion
            categoria = self.curso.categoria.nombre
            self.categoria = categoria
        super(ProgresoVideo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Progreso video'
        verbose_name_plural = 'Progreso videos'
