from django.shortcuts import render
from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer


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


