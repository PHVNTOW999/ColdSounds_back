from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Singer)
class SingersAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'registration_date',
        'id',
    )
    list_filter = [
        'username',
        'id',
    ]
    search_fields = (
        'username',
        'id',
    )

@admin.register(models.Singl)
class SinglsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
    )
    list_filter = [
        'name',
        'id',
    ]
    search_fields = (
        'name',
        'id',
    )

@admin.register(models.Album)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
    )
    list_filter = [
        'name',
        'id',
    ]
    search_fields = (
        'name',
        'id',
    )

@admin.register(models.EP)
class EPAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
    )
    list_filter = [
        'name',
        'id',
    ]
    search_fields = (
        'name',
        'id',
    )