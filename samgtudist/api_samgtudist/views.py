from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny

from api_samgtudist.models import Material
from api_samgtudist.permissions import IsAdminOrReadOnly
from api_samgtudist.serializers import MaterialSerializer


class MaterialsViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAdminOrReadOnly,)  # (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("material_title",)
