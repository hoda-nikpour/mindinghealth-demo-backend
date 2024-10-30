# patients/management/commands/import_csv.py

import csv
from django.core.management.base import BaseCommand
from patients.models import MentalDisorder

class Command(BaseCommand):
    help = 'Import data from Dataset-Mental-Disorders.csv'

    def handle(self, *args, **kwargs):
        csv_file = 'Dataset-Mental-Disorders.csv'  # Ensure the CSV file is in the correct path
        with open(csv_file, mode='r', encoding='utf-8-sig') as file:  # Use utf-8-sig to handle BOM
            reader = csv.DictReader(file)
            for row in reader:
                # Clean keys to remove any BOM or extra spaces
                cleaned_row = {k.strip(): v for k, v in row.items()}
                
                MentalDisorder.objects.create(
                    patient_number=cleaned_row['Patient Number'],
                    sadness=cleaned_row['Sadness'],
                    euphoric=cleaned_row['Euphoric'],
                    exhausted=cleaned_row['Exhausted'],
                    sleep_disorder=cleaned_row['Sleep dissorder'],
                    mood_swing=cleaned_row['Mood Swing'],
                    suicidal_thoughts=cleaned_row['Suicidal thoughts'],
                    anorexia=cleaned_row['Anorxia'],
                    authority=cleaned_row['Authority Respect'],  # Assuming this is combined in your CSV
                    respect=cleaned_row['Authority Respect'],     # Adjust this as needed
                    try_explanation=cleaned_row['Try-Explanation'],
                    aggressive_response=cleaned_row['Aggressive Response'],
                    ignore_move_on=cleaned_row['Ignore & Move-On'],
                    nervous_breakdown=cleaned_row['Nervous Break-down'],
                    admit_mistakes=cleaned_row['Admit Mistakes'],
                    overthinking=cleaned_row['Overthinking'],
                    sexual_activity=cleaned_row['Sexual Activity'],
                    concentration=cleaned_row['Concentration'],
                    optimism=cleaned_row['Optimisim'],  # Ensure this is matched correctly
                    expert_diagnosis=cleaned_row['Expert Diagnose']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
