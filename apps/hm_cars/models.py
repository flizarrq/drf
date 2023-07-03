from django.db import models

from core.models import BaseModel
from apps.auto_parks.models import AutoParkModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'hm_cars'

    brand = models.CharField(max_length=25)  # unique=True, null=True,default=0,blank=True
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
