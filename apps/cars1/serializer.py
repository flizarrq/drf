from rest_framework import serializers

from .models import CarsModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')
