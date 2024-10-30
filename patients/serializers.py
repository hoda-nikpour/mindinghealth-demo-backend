# patients/serializers.py

from rest_framework import serializers
from .models import MentalDisorder

class MentalDisorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalDisorder
        fields = '__all__'  # Or specify the fields you need
