from django.db import models

from core.models import BaseModel


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks1'

    name = models.CharField(max_length=25)
