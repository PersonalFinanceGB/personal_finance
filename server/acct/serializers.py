from .models import User_acct
from rest_framework import serializers, request


class BillSerializer(serializers.ModelSerializer):
    """
    Serializing all the Bills
    """
    class Meta:
        model = User_acct
        fields = ('id_user', 'id_acct', 'sum')

    # email = serializers.IntegerField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()

    def create(self, validated_data):
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
