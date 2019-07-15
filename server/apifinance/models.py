from django.db import models
from datetime import datetime
from datetime import date


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

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.bill_name = validated_data.get('bill_name', instance.bill_name)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance


class Transaction(models.Model):
    id = models.IntegerField(
        primary_key=True,
        verbose_name='id транзакции',
    )
    payer = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name='payer'
    )
    buyer = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name='buyer'
    )
    date_time = models.DateField(
        default=date.today
    )
    sum_contract = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.payer} -> {self.payer} = {self.sum_contract}'
