# core/urls.py

from django.urls import path
from .views import predict_performance  # Explicit import

urlpatterns = [
    path('', predict_performance, name='index'),
]
