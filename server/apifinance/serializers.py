from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    """
    Сериализация счетов
    """
    # можно использовать вместо my_extra_fiels инфу по запросившему пользователю
    my_extra_fields = serializers.SerializerMethodField('get_extra_fields')

    class Meta:
        model = Bill
        fields = ('id', 'bill_name', 'my_extra_fields', )

    def get_extra_fields(self, obj):
        tmp_dict = {
            'id': obj.id,
            'name': obj.bill_name
        }
        return tmp_dict
        # return "тест {}" .format(obj.id)

