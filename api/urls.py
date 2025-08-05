# api/urls.py

from django.urls import path
from .views import get_intern_data

urlpatterns = [
    path('data/', get_intern_data, name='get_intern_data'),
]