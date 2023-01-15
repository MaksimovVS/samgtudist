from rest_framework import viewsets, generics

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
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("material_title",)
