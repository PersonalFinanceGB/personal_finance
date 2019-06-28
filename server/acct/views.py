# from django.shortcuts import render
from rest_framework import generics
from acct.models import User_acct
from acct.serializers import BillSerializer


class BillView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = User_acct
    queryset = User_acct.objects.all()
    serializer_class = BillSerializer

