from django.shortcuts import render

# Create your views here.
def feeCollection(request):
    return render(request,'finance/fee_collection.html')


def feeCollectionDue(request):
    return render(request,'finance/fee_collection_due.html')


def feeCollectionReport(request):
    return render(request,'finance/fee_collection_report.html')
