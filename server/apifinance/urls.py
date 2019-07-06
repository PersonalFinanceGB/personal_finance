from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import BillsView


urlpatterns = [
    url(r'^bills/', BillsView.as_view(), name='bills-list'),

]
