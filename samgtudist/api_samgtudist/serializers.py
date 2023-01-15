from rest_framework import serializers
from api_samgtudist.models import Material, Picture, Paragraph


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ["id", "paragraph_text",]


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fileds = ["id", "image"]


class MaterialSerializer(serializers.ModelSerializer):
    quote_text = ParagraphSerializer(many=True, read_only=True)
    example_page = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        fields = [
            'id',
            'material_title',
            'paragraph_text',
            'image',
            'subject',
        ]