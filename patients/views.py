# patients/views.py

from rest_framework import generics
from .models import MentalDisorder
from .serializers import MentalDisorderSerializer

class MentalDisorderList(generics.ListAPIView):
    queryset = MentalDisorder.objects.all()
    serializer_class = MentalDisorderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Fetch multiple filter parameters
        sadness = self.request.query_params.get('Sadness', None)
        euphoric = self.request.query_params.get('Euphoric', None)
        exhausted = self.request.query_params.get('Exhausted', None)
        sleep_disorder = self.request.query_params.get('Sleep disorder', None)
        anorexia = self.request.query_params.get('Anorexia', None)
        concentration = self.request.query_params.get('Concentration', None)

        # Apply filters if they are provided
        if sadness:
            queryset = queryset.filter(sadness=sadness)
        if euphoric:
            queryset = queryset.filter(euphoric=euphoric)
        if exhausted:
            queryset = queryset.filter(exhausted=exhausted)
        if sleep_disorder:
            queryset = queryset.filter(sleep_disorder=sleep_disorder)
        if anorexia:
            queryset = queryset.filter(anorexia=anorexia)
        if concentration:
            queryset = queryset.filter(concentration=concentration)

        return queryset
