from django.urls import path
from . import views, api_views

app_name='credentials'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/credentials/', api_views.credential_list, name='credential_list'),
    path('api/credentials/<int:pk>/', api_views.credential_detail, name='credential_detail'),
]
