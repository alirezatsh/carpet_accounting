# Generated by Django 5.1.2 on 2024-10-14 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0018_alter_month_options_alter_year_options_month_carpets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='month',
            name='carpets',
        ),
        migrations.AddField(
            model_name='month',
            name='carpets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carpet_month', to='carpets.carpet'),
        ),
    ]
