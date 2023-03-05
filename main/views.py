from rest_framework import generics
from .models import Singer, Singl, Album, EP
from .serializers import SingerSerializer, SinglSerializer, AlbumSerializer, EPSerializer


class SingersList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SinglsList(generics.ListCreateAPIView):
    queryset = Singl.objects.all()
    serializer_class = SinglSerializer

class AlbumsList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
class EPList(generics.ListCreateAPIView):
    queryset = EP.objects.all()
    serializer_class = EPSerializer
