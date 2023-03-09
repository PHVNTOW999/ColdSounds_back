from django.contrib import admin
from django.urls import path

from main.views import SingersList, SinglsList, AlbumsList, EPList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/singers/', SingersList.as_view(), name='singers_list'),
    path('api/singls/', SinglsList.as_view(), name='singls_list'),
    path('api/albums/', AlbumsList.as_view(), name='albums_list'),
    path('api/ep/', EPList.as_view(), name='ep_list')
]
