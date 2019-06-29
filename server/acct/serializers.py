from .models import User_acct, Type_acct
from rest_framework import serializers


class AcctSerializer(serializers.ModelSerializer):
    """
    Serializing all the Type_acct
    """
    class Meta:
        model = Type_acct
        fields = ('type_acct', )

    def create(self, validated_data):
        return Type_acct.objects.create(**validated_data)


class BillSerializer(serializers.ModelSerializer):
    """
    Serializing all the Bills
    """
    class Meta:
        model = User_acct
        fields = ('id_user', 'id_acct', 'sum')

    def create(self, validated_data):
        # type_acct_data = validated_data.get('id_acct')
        # Type_acct.objects.create(**type_acct_data)
        return User_acct.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.id_user = validated_data.get('id_user', instance.id_user)
    #     instance.id_acct = validated_data.get('id_acct', instance.id_acct)
    #     instance.sum = validated_data.get('id_acct', instance.sum)
    #     return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Access self.context here to add contextual data into ret
        ret['user'] = self.context['user']
        return ret
