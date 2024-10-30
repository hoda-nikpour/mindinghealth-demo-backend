from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=100)
    case_text = models.CharField(max_length=2000)
    result = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
