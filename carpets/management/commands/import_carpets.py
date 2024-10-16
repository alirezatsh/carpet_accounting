import json
from django.core.management.base import BaseCommand
from carpets.models import Carpet, Color, Design, Length, Width 
from accounts.models import Workers

class Command(BaseCommand):
    help = 'Import carpets from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('accounting\\carpet_data.json', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['accounting\\carpet_data.json']

        # خواندن فایل JSON
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                carpets_data = json.load(file)

                for carpet in carpets_data:
                    try:
                        # ایجاد فرش جدید
                        Carpet.objects.create(
                            rang=Color.objects.get(id=carpet['rang']),
                            naghsheh=Design.objects.get(id=carpet['naghsheh']),
                            tool=Length.objects.get(id=carpet['tool']),
                            arz=Width.objects.get(id=carpet['arz']),
                            isRectangle=carpet['isRectangle'],
                            metraj=carpet['metraj'],
                            serial=carpet['serial'],
                            code=carpet['code'],
                            shirazeh=Workers.objects.get(id=carpet['shirazeh']),
                            cheleh=Workers.objects.get(id=carpet['cheleh']),
                            gereh=Workers.objects.get(id=carpet['gereh']),
                            shirazehKhoroug=carpet['shirazehKhoroug'],
                            chelehKhoroug=carpet['chelehKhoroug'],
                            grehKhoroug=carpet['grehKhoroug'],
                            shirazehVouroud=carpet['shirazehVouroud'],
                            chellehVouroud=carpet['chellehVouroud'],
                            gerehVouroud=carpet['gerehVouroud'],
                            ersalshodeh=carpet['ersalshodeh']
                        )
                        self.stdout.write(self.style.SUCCESS(f'Successfully added carpet {carpet["serial"]}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error adding carpet {carpet["serial"]}: {e}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))
