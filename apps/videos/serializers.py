from . import models
from apps.utils.serializers import CustomSerializer
from rest_framework import serializers


class CategoriaSerializer(CustomSerializer):
    class Meta:
        model = models.Categoria
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class CursoSerializer(CustomSerializer):
    class Meta:
        model = models.Curso
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class InscripcionSerializer(CustomSerializer):
    class Meta:
        model = models.Inscripcion
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class ProgresoVideoSerializer(CustomSerializer):
    class Meta:
        model = models.ProgresoVideo
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]