from django.urls import path
from .views import *

app_name = 'api_samgtudist'

urlpatterns = [
    path('materials/', MaterialAPIView.as_view(), name='show_materials'),

]