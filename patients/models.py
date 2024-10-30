# patients/models.py

from django.db import models

class MentalDisorder(models.Model):
    patient_number = models.CharField(max_length=50, unique=True)
    sadness = models.CharField(max_length=50)
    euphoric = models.CharField(max_length=50)
    exhausted = models.CharField(max_length=50)
    sleep_disorder = models.CharField(max_length=50)
    mood_swing = models.CharField(max_length=50)
    suicidal_thoughts = models.CharField(max_length=50)
    anorexia = models.CharField(max_length=50)
    authority = models.CharField(max_length=50)
    respect = models.CharField(max_length=50)
    try_explanation = models.CharField(max_length=50)
    aggressive_response = models.CharField(max_length=50)
    ignore_move_on = models.CharField(max_length=50)
    nervous_breakdown = models.CharField(max_length=50)
    admit_mistakes = models.CharField(max_length=50)
    overthinking = models.CharField(max_length=50)
    sexual_activity = models.CharField(max_length=50)
    concentration = models.CharField(max_length=50)
    optimism = models.CharField(max_length=50)
    expert_diagnosis = models.CharField(max_length=50)

    def __str__(self):
        return self.patient_number
