from rest_framework import status, viewsets
from rest_framework.response import Response

from . import models, serializers


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    model = models.Categoria


class CursoViewSet(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer
    model = models.Curso


class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = models.Inscripcion.objects.all()
    serializer_class = serializers.InscripcionSerializer
    model = models.Inscripcion


class ProgresoVideoViewSet(viewsets.ModelViewSet):
    queryset = models.ProgresoVideo.objects.all()
    serializer_class = serializers.ProgresoVideoSerializer
    model = models.ProgresoVideo
