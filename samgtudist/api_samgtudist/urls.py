from django.urls import include, path
from rest_framework import routers

from api_samgtudist.views import MaterialsViewSet

app_name = 'api_samgtudist'

router_v1 = routers.DefaultRouter()

router_v1.register("materials", MaterialsViewSet, basename="material")


urlpatterns = [
    # path('materials/', MaterialAPIView.as_view(), name='show_materials'),
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
