from django.urls import include, path
from rest_framework import routers

from api_samgtudist import views  

app_name = 'api_samgtudist'

router_v1 = routers.DefaultRouter()

router_v1.register('index', views.IndexPageViewSet, basename="index")
router_v1.register("material", views.MaterialViewSet, basename="material")
router_v1.register("subject_list",
                   views.SubjectListViewSet, basename="subject_list")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
