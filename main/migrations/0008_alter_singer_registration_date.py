# Generated by Django 4.1.7 on 2023-02-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_singer_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='registration_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Registration Date'),
        ),
    ]
