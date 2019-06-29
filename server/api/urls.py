from django.urls import include, path
from django.conf.urls import url
import acct.views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^bills/$', acct.views.BillView.as_view()),
    url(r'^bills/type/$', acct.views.TypeBillView.as_view())
]
