from rest_framework import serializers

from apps.cars1.serializer import CarSerializer

from .models import AutoParkModel


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
