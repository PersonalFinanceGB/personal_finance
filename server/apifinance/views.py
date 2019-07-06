from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Bill
from .serializers import BillSerializer


class BillsView(ListAPIView):
    """
    Returns a list of all bills.
    """
    model = Bill
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillsInstanceView(RetrieveAPIView):
    """
    Returns a single bill.
    Also allows updating and deleting
    """
    model = Bill
    serializer_class = BillSerializer

    def get_queryset(self):
        return Bill.objects.all()

