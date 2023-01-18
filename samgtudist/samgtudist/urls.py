from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/',
        include('api_samgtudist.urls', namespace="api_samgtudist")
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#временное решение, чтобы показывать статические файлы без внешнего сервера
#обязательно убрать в продакшене!!