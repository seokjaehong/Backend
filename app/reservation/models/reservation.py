from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import F
from rest_framework.exceptions import APIException

from members.models import *
from reservation.models.reservation_base import ReservationBase

from travel.models import TravelSchedule

__all__ = (
    'Reservation',
)
User = get_user_model()


#  해당 상품이 위시리스트에 있는지 체크
class PeopleOverMaxValueExists(APIException):
    status_code = 400
    default_detail = '최대 예약가능한 인원을 초과했습니다.'


class ReservationManager(models.Manager):
    def validate_is_possible_reservation(self, people, max):
        if people <= max:
            return True
        return False

    def create_with_schedule(self, *args, **kwargs):
        travel_schedule, _ = TravelSchedule.objects.get_or_create(
            travel_info=kwargs["travel_info"],
            start_date=kwargs["start_date"],
        )
        max_people = travel_schedule.travel_info.max_people

        reserve_user_sum = kwargs['people'] + travel_schedule.reserved_people

        if self.validate_is_possible_reservation(reserve_user_sum, max_people):
            travel_schedule.reserved_people += reserve_user_sum
            travel_schedule.save()
        else:
            raise PeopleOverMaxValueExists

        reservation = Reservation.objects.create(
            travel_schedule=travel_schedule,
            member=kwargs["member"],
            people=kwargs['people'],
        )
        return reservation


class Reservation(ReservationBase):
    travel_schedule = models.ForeignKey(
        TravelSchedule,
        on_delete=models.CASCADE,
        verbose_name='travel_schedule'
    )
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='user'
    )
    is_canceled = models.BooleanField('취소여부', default=False)
    people = models.IntegerField('예약수', default=1)
    concept = models.TextField('여행컨셉', blank=True)
    age_generation = models.CharField('연령대', blank=True, max_length=50)
    personal_request = models.TextField('요청사항', blank=True)

    class Meta:
        app_label = 'reservation'

    @property
    def total_price(self):
        return self.people * self.travel_schedule.travel_info.price

    objects = ReservationManager()
