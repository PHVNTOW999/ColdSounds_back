# Generated by Django 4.1.7 on 2023-02-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_singl_release_date_singl_auditions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singl',
            name='auditions',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Singl_auditions'),
        ),
    ]
