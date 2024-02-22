# Generated by Django 4.2.6 on 2023-11-02 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.participant')),
            ],
        ),
        migrations.RemoveField(
            model_name='race',
            name='race_results',
        ),
        migrations.DeleteModel(
            name='RaceResult',
        ),
        migrations.AddField(
            model_name='raceregistration',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.race'),
        ),
        migrations.AddField(
            model_name='participant',
            name='registered_races',
            field=models.ManyToManyField(through='race.RaceRegistration', to='race.race'),
        ),
        migrations.AddField(
            model_name='race',
            name='registered_participants',
            field=models.ManyToManyField(through='race.RaceRegistration', to='race.participant'),
        ),
    ]
