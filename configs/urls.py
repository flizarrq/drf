from django.urls import path, include

urlpatterns = [
    path('cars', include('apps.cars1.urls')),
    path('auto_parks', include('apps.auto_parks1.urls')),

]
