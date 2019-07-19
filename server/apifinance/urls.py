from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import (BillsView,
                    BillsInstanceView,
                    TransactionView,
                    TransactionInstanceView)


urlpatterns = [
    url(r'^bills/$', BillsView.as_view(), name='bills-list'),
    url(r'^bills/(?P<pk>[\d]+)/$', BillsInstanceView.as_view(),
        name='bills-instanse'),
    url(r'^trank/$', TransactionView.as_view(), name='transaction-list'),
    url(r'^trank/(?P<pk>[\d]+)/$', TransactionInstanceView.as_view(),
        name='transaction-instanse'),
]

