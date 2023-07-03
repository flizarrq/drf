from django.urls import path

from apps.hm_cars.views import CarListCreateView, CarReadUpdateDelete

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarReadUpdateDelete.as_view())
]
