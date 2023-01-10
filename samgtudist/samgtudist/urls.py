from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/',
        include('api_samgtudist.urls', namespace="api_samgtudist")
    ),
]
