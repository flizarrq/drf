from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import CarModel
from .serializer import CarBaseSerializer


# CRUD
# Create
# Read
# Update
# Delete

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarBaseSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarBaseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarReadUpdateDelete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarBaseSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        data = self.request.data
        serializer = CarBaseSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarBaseSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
        return Response('deleted',status.HTTP_204_NO_CONTENT)
