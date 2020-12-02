from django.urls import path, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'categorias', viewsets.CategoriaViewSet)
router.register(r'cursos', viewsets.CursoViewSet)
router.register(r'inscripciones', viewsets.InscripcionViewSet)
router.register(r'progreso_videos', viewsets.ProgresoVideoViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]