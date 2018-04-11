from django.contrib.auth import get_user_model
from django.db import models

from .product_base import ProductBase
from .travel_information import TravelInformation

User = get_user_model()

__all__ = (
    'TravelSchedule',
)


class TravelSchedule(ProductBase):
    travel_info = models.ForeignKey(
        TravelInformation,
        on_delete=models.CASCADE,
        verbose_name='travel_info')
    travelschedule_user = models.ManyToManyField(User, through='reservation.Reservation')

    reserved_people = models.IntegerField(default=0)
    start_date = models.DateField('여행시작날짜')
    end_date = models.DateField('여행끝날짜', blank=True, null=True)

    class Meta:
        ordering = ['-creation_datetime']

    def __str(self):
        return self.pk
