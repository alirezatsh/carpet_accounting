# Generated by Django 5.1.2 on 2024-10-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0003_length_radius_width_carpet_length_carpet_radius_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpet',
            name='is_rectangle',
            field=models.BooleanField(default=True, verbose_name='مستطیل'),
        ),
    ]
