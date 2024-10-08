from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CredentialViewSet

router = DefaultRouter()
router.register(r'credentials', CredentialViewSet, basename='credential')

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('api/', include(router.urls)), 
]

