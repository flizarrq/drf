from django.urls import path, include


urlpatterns = [
    path('cars', include('apps.hm_cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls'))
]
