# from django.shortcuts import render
from rest_framework import generics, request
from acct.models import User_acct, Type_acct
from acct.serializers import BillSerializer, AcctSerializer


class BillView(generics.ListCreateAPIView):
    """
    Returns a list of all bills.
    """
    model = User_acct
    queryset = User_acct.objects.all()
    serializer_class = BillSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = 'добавим данные запросившего пользователя'
        return context


class TypeBillView(generics.ListCreateAPIView):
    """
    Returns a list of all type bills.
    """
    model = Type_acct
    queryset = Type_acct.objects.all()
    serializer_class = AcctSerializer
