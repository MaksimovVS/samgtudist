from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from api_samgtudist.models import Material, Subject
from api_samgtudist.permissions import IsAdminOrReadOnly
from api_samgtudist import serializers


class IndexPageViewSet(ReadOnlyModelViewSet):
    """Передаем список предметов. Главная страница."""
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectListSerializer
    permission_classes = (IsAdminOrReadOnly,)


class MaterialViewSet(ReadOnlyModelViewSet):
    """Передает информацию о работах.Вторая и Третья страница."""
    queryset = Material.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("material_title", "paragraph__paragraph_text")

    def get_serializer_class(self):
        if self.kwargs.get('pk', None):
            return serializers.MaterialDetailSerializer
        return serializers.MaterialSerializer

    def get_queryset(self):
        return Material.objects.filter(subject=self.kwargs.get('subject_id'))
