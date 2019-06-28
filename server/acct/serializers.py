from .models import User_acct
from rest_framework import serializers, request


class BillSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = User_acct
        fields = ('id_user', 'id_acct', 'sum')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Access self.context here to add contextual data into ret
        ret['user'] = self.context['user']
        return ret
