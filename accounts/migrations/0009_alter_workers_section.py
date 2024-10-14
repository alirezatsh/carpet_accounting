# Generated by Django 5.1.2 on 2024-10-12 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_workers_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='accounts.section', verbose_name='بخش'),
        ),
    ]