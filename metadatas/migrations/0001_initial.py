# Generated by Django 4.1.7 on 2023-03-09 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, verbose_name="Menu's link name")),
                ('path', models.CharField(max_length=500, verbose_name="Menu's link path")),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
    ]
