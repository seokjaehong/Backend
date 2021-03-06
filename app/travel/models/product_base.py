from django.utils import timezone
from django.db import models

__all__ = (
    'ProductBase',
)


class ProductBase(models.Model):
    is_usable = models.BooleanField('사용여부', default=True)
    creation_datetime = models.DateTimeField('생성시간', default=timezone.now)
    modify_datetime = models.DateTimeField('수정시간', default=timezone.now)

    class Meta:
        abstract = True
