from django.urls import path
from .views import CaseList

urlpatterns = [
    path('casesinfo/', CaseList.as_view(), name='case-list'),
]
