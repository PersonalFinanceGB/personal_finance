from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import BillsView, BillsInstanceView


urlpatterns = [
    url(r'^bills/$', BillsView.as_view(), name='bills-list'),
    url(r'^bills/(?P<pk>[\d]+)/$', BillsInstanceView.as_view(),
        name='bills-instanse'),
]
