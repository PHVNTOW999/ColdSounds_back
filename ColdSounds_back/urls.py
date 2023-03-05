from django.contrib import admin
from django.urls import path

from main.views import SingersList, SinglsList, AlbumsList, EPList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singers/', SingersList.as_view(), name='singers_list'),
    path('singls/', SinglsList.as_view(), name='singls_list'),
    path('albums/', AlbumsList.as_view(), name='albums_list'),
    path('ep/', EPList.as_view(), name='ep_list')
]
