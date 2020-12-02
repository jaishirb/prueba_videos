
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.utils.shortcuts import get_object_or_none
from . import models


@receiver(post_save, sender=models.ProgresoVideo)
def relacionar_data(sender, instance, created, **kwargs):
    if created:
        inscripcion = get_object_or_none(
            models.Inscripcion,
            usuario=instance.usuario,
            curso=instance.curso
        )
        if inscripcion:
            instance.inscripcion = inscripcion
        categoria = instance.curso.categoria.nombre
        instance.categoria = categoria
        instance.save()