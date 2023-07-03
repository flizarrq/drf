from rest_framework import serializers

from .models import CarModel


class CarBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')

