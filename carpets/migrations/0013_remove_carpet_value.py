# Generated by Django 5.1.2 on 2024-10-14 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0012_rename_chelehkhoroug_carpet_chelehkhoroug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpet',
            name='value',
        ),
    ]
