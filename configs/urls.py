from django.urls import path
from hm_cars.views import CarListCreateView, CarReadUpdateDelete

urlpatterns = [
    path('cars', CarListCreateView.as_view()),
    path('cars/<int:pk>', CarReadUpdateDelete.as_view())
]
