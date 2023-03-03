from rest_framework import generics
from .models import Singer, Singl
from .serializers import SingerSerializer, SinglSerializer


class SingersList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SinglsList(generics.ListCreateAPIView):
    queryset = Singl.objects.all()
    serializer_class = SinglSerializer
