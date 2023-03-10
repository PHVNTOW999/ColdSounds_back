from rest_framework import generics

from .models import Menu
from .serializers import MenuSerializer


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer