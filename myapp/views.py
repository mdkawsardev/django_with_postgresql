from django.shortcuts import render
from .models import Mycontact
# Create your views here.
def home(request):
    context = {
        'contexts': Mycontact.objects.all()
    }
    return render(request, 'index.html', context)