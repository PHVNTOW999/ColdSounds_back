from django.db import models


class Singer(models.Model):
    id = models.AutoField(primary_key=True)

    username = models.CharField(
        max_length=30,
        verbose_name='Nickname',
        null=False,
        blank=False,
    )

    registration_date = models.DateField(
        auto_now=True,
        verbose_name="Registration Date",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Singer'
        verbose_name_plural = 'Singers'

class Singl(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=30,
        verbose_name='Singl',
        null=False,
        blank=False,
    )

    singers = models.ManyToManyField(
        Singer,
        verbose_name="Singl_Singers",
        null=False,
        blank=False,
    )

    feat = models.ManyToManyField(
        Singer,
        verbose_name="Singl_feat",
        related_name="Singl_feat",
        null=True,
        blank=True,
    )

    auditions = models.IntegerField(
        default=0,
        verbose_name="Singl_auditions",
        null=True,
        blank=True,
    )

    downloads = models.IntegerField(
        default=0,
        verbose_name="Singl_downloads",
        null=True,
        blank=True,
    )

    registration_date = models.DateField(
        auto_now=True,
        verbose_name="Release Date",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Singl'
        verbose_name_plural = 'Singls'