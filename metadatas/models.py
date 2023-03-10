from django.db import models

# Create your models here.

class Menu(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=15,
        verbose_name="Menu's link name",
        null=False,
        blank=False,
    )

    path = models.CharField(
        max_length=500,
        verbose_name="Menu's link path",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
