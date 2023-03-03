from rest_framework import serializers
from .models import Singer, Singl


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"

class SinglSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singl
        fields = "__all__"
