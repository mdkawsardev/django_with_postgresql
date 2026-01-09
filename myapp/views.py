from django.shortcuts import render
from .models import Mycontact, Myusers, Customers
from django.contrib import messages
# Create your views here.
def home(request):
    allData = {
        'contexts1': Mycontact.objects.all(),
        'contexts2': Myusers.objects.all(),
        'contexts3': Customers.objects.all(),
    }
    return render(request, 'index.html', allData)
def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Mycontact.objects.create(
            name = name,
            email = email,
            phone = phone
        )
        #? Same as above
        # con = Mycontact(
        #     name = name,
        #     email = email,
        #     phone = phone
        # )
        # con.save()
        # msg = messages.success(request, "Data has been recorded!")
    return render(request, 'insert.html')