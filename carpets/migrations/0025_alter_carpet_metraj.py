# Generated by Django 5.1.2 on 2024-10-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0024_alter_carpet_metraj_alter_width_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpet',
            name='metraj',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='متراژ'),
        ),
    ]
