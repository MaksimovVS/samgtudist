from rest_framework import viewsets, filters
from rest_framework.generics import RetrieveAPIView, ListAPIView

from api_samgtudist.models import Material, Subject
from api_samgtudist.permissions import IsAdminOrReadOnly
from api_samgtudist import serializers


class IndexPageViewSet(ListAPIView, viewsets.GenericViewSet):
    """Передаем список предметов. Главная страница."""
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = (IsAdminOrReadOnly,)


class SubjectListViewSet(RetrieveAPIView, viewsets.GenericViewSet):
    """Передаем список работ по предмету. Вторая страница."""
    queryset = Material.objects.all()
    serializer_class = serializers.SubjectListSerializer
    permission_classes = (IsAdminOrReadOnly,)


class MaterialViewSet(RetrieveAPIView, viewsets.GenericViewSet):
    """Передает информацию о работе. Третья страница."""
    queryset = Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("material_title",)
