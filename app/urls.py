from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('resultado/', views.verDominio, name='verDominio'),
]
