# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('containers/new/', views.create_container, name='create_container'),
    path('containers/<int:container_id>/', views.container_detail, name='container_detail'),
    path('containers/<int:container_id>/qr/', views.generate_qr, name='generate_qr'),
]
