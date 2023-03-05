from rest_framework import serializers
from .models import Singer, Singl, Album, EP


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"

class SinglSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singl
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
class EPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EP
        fields = "__all__"
