# from django.shortcuts import render
from rest_framework import generics, request
from rest_framework.request import Request
from acct.models import User_acct
from acct.serializers import BillSerializer


class BillView(generics.ListCreateAPIView):
    """
    Returns a list of all authors.
    """
    model = User_acct
    queryset = User_acct.objects.all()
    serializer_class = BillSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = str('какие-то данные')
        return context

