from django.urls import path
from .views import scan_image_view

urlpatterns = [
    path('', scan_image_view, name='scan_image'),
]
