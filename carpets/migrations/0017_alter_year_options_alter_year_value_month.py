# Generated by Django 5.1.2 on 2024-10-14 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0016_alter_year_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='year',
            options={},
        ),
        migrations.AlterField(
            model_name='year',
            name='value',
            field=models.IntegerField(unique=True, verbose_name='سال'),
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], verbose_name='ماه')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='months', to='carpets.year')),
            ],
            options={
                'verbose_name': 'سال\u200cها',
            },
        ),
    ]
