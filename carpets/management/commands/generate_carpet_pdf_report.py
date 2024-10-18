import csv
from django.core.management.base import BaseCommand
from carpets.models import Carpet

class Command(BaseCommand):
    help = 'Generate a CSV report for all carpets'

    def handle(self, *args, **kwargs):
        file_path = 'carpet_report.csv'
        
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Carpet' ])  # نوشتن هدر

            carpets = Carpet.objects.all()
            for carpet in carpets:
                writer.writerow([carpet.serial, carpet.naghsheh, carpet.rang, carpet.tool, carpet.arz , carpet.id , carpet.shirazeh])

        self.stdout.write(self.style.SUCCESS(f'CSV report generated successfully: {file_path}'))
