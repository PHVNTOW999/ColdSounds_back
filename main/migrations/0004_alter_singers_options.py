# Generated by Django 4.1.7 on 2023-02-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_singers_delete_singer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='singers',
            options={'verbose_name': 'Singer', 'verbose_name_plural': 'Singers'},
        ),
    ]
