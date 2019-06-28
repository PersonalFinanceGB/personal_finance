from .models import User_acct
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = User_acct
        fields = ('id_user', 'id_acct', 'sum')

