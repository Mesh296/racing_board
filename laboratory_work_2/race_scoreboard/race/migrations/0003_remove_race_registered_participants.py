# Generated by Django 4.2.6 on 2023-11-02 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0002_raceregistration_remove_race_race_results_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='registered_participants',
        ),
    ]
