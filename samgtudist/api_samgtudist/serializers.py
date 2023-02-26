from rest_framework import serializers
from .models import Material, Picture, Paragraph, Subject


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ("paragraph_text",)


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("image",)


class MaterialDetailSerializer(serializers.ModelSerializer):
    paragraph_text = ParagraphSerializer(
        many=True,
        read_only=True,
        source="paragraph"
        )
    image = PictureSerializer(
        many=True,
        source="images"
        )

    class Meta:
        model = Material
        fields = [
            'subject',
            'id',
            'material_title',
            'paragraph_text',
            'image',
        ]


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["id", "material_title", "material_type"]


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "subject_title"]


class ParagraphSearchSerializer(serializers.ModelSerializer):
    material = MaterialSerializer

    class Meta:
        model = Paragraph
        fields = ('material', 'paragraph_text')


class PopularMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ("id", "material_title", "material_type")
