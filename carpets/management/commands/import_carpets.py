import json
from django.core.management.base import BaseCommand
from carpets.models import Carpet
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
                            rang=carpet['rang'],  # رشته
                            naghsheh=carpet['naghsheh'],  # رشته
                            tool=carpet['tool'],  # رشته
                            arz=carpet['arz'],  # رشته
                            isRectangle=carpet['isRectangle'],  # بولین
                            metraj=carpet['metraj'],  # رشته
                            serial=carpet['serial'],  # رشته
                            code=carpet['code'],  # رشته
                            shirazeh=carpet['shirazeh'],  # رشته
                            cheleh=carpet['cheleh'],  # رشته
                            gereh=carpet['gereh'],  # رشته
                            shirazehKhoroug=carpet['shirazehKhoroug'],  # رشته (تاریخ یا استرینگ)
                            chelehKhoroug=carpet.get('chelehKhoroug', ''),  # رشته
                            grehKhoroug=carpet['gerehKhoroug'],  # رشته
                            shirazehVouroud=carpet['shirazehVouroud'],  # رشته
                            chellehVouroud=carpet.get('chellehVouroud', ''),  # رشته
                            gerehVouroud=carpet['gerehVouroud'],  # رشته
                            ersalshodeh=carpet['ersalshodeh']  # بولین
                        )
                        self.stdout.write(self.style.SUCCESS(f'Successfully added carpet {carpet["serial"]}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error adding carpet {carpet["serial"]}: {e}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))



