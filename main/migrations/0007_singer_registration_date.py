# Generated by Django 4.1.7 on 2023-02-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_song_singers'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='registration_date',
            field=models.DateField(auto_now=True, verbose_name='Registration Date'),
        ),
    ]
