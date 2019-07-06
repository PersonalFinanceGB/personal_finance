from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Bill
from .serializers import BillSerializer


class BillsView(ListAPIView):
    """
    Returns a list of all bills.
    """
    model = Bill
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
