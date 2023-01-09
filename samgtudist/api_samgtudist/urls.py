from django.urls import path
from .views import MaterialAPIView

app_name = 'api_samgtudist'

urlpatterns = [
    path('materials/', MaterialAPIView.as_view(), name='show_materials'),
]
