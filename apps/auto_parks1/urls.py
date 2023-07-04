from django.urls import path
from .views import AutoCarReadCreateView, AutoCarRetrieveUpdateDestroyView, AutoParkCarListCreateView

urlpatterns = [
    path('', AutoCarReadCreateView.as_view()),
    path('/<int:pk>', AutoCarRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view())
]
