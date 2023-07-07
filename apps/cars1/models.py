from django.db import models

from core.models import BaseModel

from apps.auto_parks1.models import AutoParkModel


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars1'
        ordering = ('id',)

    brand = models.CharField(max_length=25)
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
