# Generated by Django 5.1.2 on 2024-10-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='workers',
            name='landline_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن ثابت'),
        ),
        migrations.AddField(
            model_name='workers',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='تلفن'),
        ),
    ]
