# Generated by Django 5.1.2 on 2024-10-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0010_remove_carpet_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpet',
            name='value',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='فرش ها'),
        ),
    ]
