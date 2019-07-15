from django.shortcuts import render
from rest_framework import generics, response, request
from .models import Bill, Transaction
from .serializers import BillSerializer, TransactionSerializer


class BillsView(generics.ListCreateAPIView):
    """
    Returns a list of all bills.
    """
    model = Bill
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillsInstanceView(generics.RetrieveUpdateAPIView):
    """
    Returns a single bill.
    Also allows updating and deleting
    """
    model = Bill
    serializer_class = BillSerializer

    def get_queryset(self):
        return Bill.objects.all()


class TransactionView(generics.ListCreateAPIView):
    """
    Returns a list of all Transactions.
    """
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionInstanceView(generics.RetrieveUpdateAPIView):
    model = Transaction
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.all()

    # def post(self, *args, **kwargs):
    #     print(args, '\n', kwargs)
    #     return response.Response
