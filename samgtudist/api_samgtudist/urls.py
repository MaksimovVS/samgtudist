from django.urls import include, path
from rest_framework import routers

from api_samgtudist import views

app_name = 'api_samgtudist'

router_v1 = routers.DefaultRouter()

router_v1.register('index', views.IndexPageViewSet)
router_v1.register(r'search/(?P<search_word>\w+)', views.SearchListAPIView,
                   basename='search')
router_v1.register(r"(?P<subject_id>\d+)/material", views.MaterialViewSet)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
