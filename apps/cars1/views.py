from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .filters import car_filtered_queryset
from .models import CarsModel
from .serializer import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    # pagination_class = PageNumberPagination

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()
