from django.urls import path
from .views import scan_image_view

app_name = 'image_scanner'

urlpatterns = [
    path('', scan_image_view, name='scan_image'),
]
