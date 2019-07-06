from django.db import models
from datetime import datetime


class Bill(models.Model):
    id = models.IntegerField(
        primary_key=True,
        verbose_name='уникальный ручной id счета'
    )
    bill_name = models.CharField(
        verbose_name='название счета',
        max_length=128,
        unique=True
    )

    def __str__(self):
        return self.bill_name
