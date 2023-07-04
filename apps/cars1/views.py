from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .serializer import CarSerializer
from .filters import car_filtered_queryset
from .models import CarsModel


class CarListView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()
