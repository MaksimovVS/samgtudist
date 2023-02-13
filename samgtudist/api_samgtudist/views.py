from django.contrib.postgres.search import SearchVector
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from api_samgtudist.models import Material, Subject, Paragraph
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


class SearchListAPIView(ViewSet, ListAPIView):
    """Представление для отображения результатов поиска по Тестам."""
    serializer_class = serializers.ParagraphSearchSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        return Paragraph.objects.annotate(
            search=SearchVector('paragraph_text', 'material__material_title')
        ).filter(search=self.kwargs.get('search_word'))
