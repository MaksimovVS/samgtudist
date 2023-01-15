from rest_framework import generics


from .models import Material
from . serializers import MaterialSerializer


class MaterialAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
