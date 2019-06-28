# from django.shortcuts import render
from rest_framework import generics, request
from acct.models import User_acct
from acct.serializers import BillSerializer


class BillView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = User_acct
    queryset = User_acct.objects.all()
    serializer_class = BillSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['test'] = 'test'
    #     return context
    #
    # def get_renderer_context(self):
    #     context = super().get_renderer_context()
    #     context['foo'] = 'bar'
    #     return context
