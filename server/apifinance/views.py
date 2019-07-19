from django.shortcuts import render
from rest_framework import generics
from .models import Bill, Transaction
from .serializers import BillSerializer, TransactionSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


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


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
