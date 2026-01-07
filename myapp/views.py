from django.shortcuts import render
from .models import Mycontact, Myusers, Customers
# Create your views here.
def home(request):
    allData = {
        'contexts1': Mycontact.objects.all(),
        'contexts2': Myusers.objects.all(),
        'contexts3': Customers.objects.all(),
    }
    return render(request, 'index.html', allData)