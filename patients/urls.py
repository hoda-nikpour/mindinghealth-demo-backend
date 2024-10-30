# patients/urls.py

from django.urls import path
from .views import MentalDisorderList

urlpatterns = [
    path('mental-disorders/', MentalDisorderList.as_view(), name='mental-disorder-list'),  # No 'api/' prefix here
]
