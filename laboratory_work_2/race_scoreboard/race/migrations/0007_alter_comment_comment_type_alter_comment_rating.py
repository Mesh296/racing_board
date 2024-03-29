# Generated by Django 4.2.6 on 2023-11-04 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0006_remove_participant_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(choices=[('Cooperation', 'Questions about cooperation'), ('Racing', 'Questions about racing'), ('Other', 'Other')], default='Other', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
