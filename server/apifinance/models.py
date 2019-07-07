from django.db import models
from datetime import datetime


class Bill(models.Model):
    id = models.IntegerField(
        primary_key=True,
        verbose_name='id счета'
    )
    bill_name = models.CharField(
        verbose_name='название счета',
        max_length=128,
        unique=True
    )
    balance = models.DecimalField(
        default=0,
        verbose_name='доступный баланс',
        max_digits=20,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.bill_name} ({self.balance} руб.)'
