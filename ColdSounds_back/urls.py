from django.contrib import admin
from django.urls import path

from main.views import SingersList, SinglsList, AlbumsList, EPList
from metadatas.views import MenuList

urlpatterns = [
    path('admin/', admin.site.urls),

    # main
    path(r'api/singers/', SingersList.as_view(), name='singers_list'),
    path(r'api/singls/', SinglsList.as_view(), name='singles_list'),
    path(r'api/albums/', AlbumsList.as_view(), name='albums_list'),
    path(r'api/ep/', EPList.as_view(), name='ep_list'),

    # metadatas
    path('api/menu/', MenuList.as_view(), name='menu_list')
]
