# Generated by Django 5.1.2 on 2024-10-16 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0029_carpet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpet',
            name='cheleh',
        ),
        migrations.RemoveField(
            model_name='carpet',
            name='gereh',
        ),
        migrations.RemoveField(
            model_name='carpet',
            name='shirazeh',
        ),
    ]
