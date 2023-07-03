from rest_framework.generics import get_object_or_404, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from filters import car_filtered_queryset
from .models import CarModel
from .serializer import CarBaseSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarBaseSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)

    # def get(self, *args, **kwargs):
    #     qs = car_filtered_queryset(self.request.query_params)
    #     serializer = CarBaseSerializer(qs, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # post removed

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = CarBaseSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)


class CarReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CarBaseSerializer
    queryset = CarModel.objects.all()

    # def get(self, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     # car = get_object_or_404(CarModel, pk=pk)
    #
    #     car = self.get_object()
    #     serializer = CarBaseSerializer(car)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def put(self, *args, **kwargs):
    #     car = self.get_object()
    #     data = self.request.data
    #     serializer = CarBaseSerializer(car, data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def patch(self, *args, **kwargs):
    #     car = self.get_object()
    #     data = self.request.data
    #     serializer = CarBaseSerializer(car, data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def delete(self, *args, **kwargs):
    #     car = self.get_object()
    #     car.delete()
    #     return Response('deleted', status.HTTP_204_NO_CONTENT)

