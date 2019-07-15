from rest_framework import serializers
from .models import Bill, Transaction


class BillSerializer(serializers.ModelSerializer):
    """
    Сериализация счетов
    """
    # можно использовать вместо my_extra_fiels инфу по запросившему пользователю
    my_extra_fields = serializers.SerializerMethodField('get_extra_fields')

    class Meta:
        model = Bill
        fields = ('id',
                  'bill_name',
                  'balance',
                  'my_extra_fields', )

    def get_extra_fields(self, obj):
        tmp_dict = {
            'id': obj.id,
            'name': obj.bill_name
        }
        return tmp_dict

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.bill_name = validated_data.get('bill_name', instance.bill_name)
    #     instance.balance = validated_data.get('balance', instance.balance)
    #     instance.save()
    #     return instance


class TransactionSerializer(serializers.ModelSerializer):
    """
    Сериализация транзакции
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Transaction
        fields = ('id',
                  'payer',
                  'buyer',
                  'date_time',
                  'sum_contract',)

    def create(self, validated_data):
        instance_payer = validated_data['payer']
        data = {
            "id": instance_payer.id,
            "bill_name": instance_payer.bill_name,
            "balance": instance_payer.balance - validated_data['sum_contract']
        }
        instance_payer.update(instance_payer, validated_data=data)
        instance_buyer = validated_data['buyer']
        data = {
            "id": instance_buyer.id,
            "bill_name": instance_buyer.bill_name,
            "balance": instance_buyer.balance + validated_data['sum_contract']
        }
        instance_buyer.update(instance_buyer, validated_data=data)
        return Transaction.objects.create(**validated_data)

