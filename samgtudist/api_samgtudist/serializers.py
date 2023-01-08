from rest_framework import serializers
from .models import Material, Quote, ExamplePage, Content, Subject


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quote_text',)


class ExamplePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamplePage
        fields = ("page",)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("content_text",)


class MaterialSerializer(serializers.ModelSerializer):
    quote_text = QuotesSerializer(many=True, read_only=True, source="quotes")
    example_page = ExamplePageSerializer(many=True, read_only=True)
    content_text = ContentSerializer(read_only=True)

    class Meta:
        model = Material
        fields = [
            'id',
            'material_title',
            'quote_text',
            'example_page',
            'content_text',
            'subject',
        ]
