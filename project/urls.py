from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
schema_view = get_swagger_view(title='Topping api v1')
PREFIX_URL = settings.PREFIX_URL

urlpatterns = [
    path('', schema_view),
    path('{}api/'.format(PREFIX_URL), include(router.urls)),
    path('{}auth/'.format(PREFIX_URL), include('rest_auth.urls')),
    path('{}api/v1/videos/'.format(PREFIX_URL), include('apps.videos.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

