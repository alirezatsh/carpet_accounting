# Generated by Django 5.1.2 on 2024-10-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpets', '0017_alter_year_options_alter_year_value_month'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='month',
            options={},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'verbose_name': 'سال\u200cها'},
        ),
        migrations.AddField(
            model_name='month',
            name='carpets',
            field=models.ManyToManyField(blank=True, related_name='months', to='carpets.carpet'),
        ),
    ]
