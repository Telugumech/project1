from django.urls import path
from finance.views import feeCollection
from finance.views import feeCollectionDue
from finance.views import feeCollectionReport

urlpatterns = [

    path('feecoll/', feeCollection),
    path('feecolldue/', feeCollectionDue),
    path('feecollreport/', feeCollectionReport),
]
