# Generated by Django 5.1.2 on 2024-10-11 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_workers_last_name_alter_workers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.section'),
        ),
    ]
