from django.shortcuts import render, redirect
from . models import *
# Create your views here.

def homepage(request):
    prot = Prot.objects.all()
    context = {
        'prot': prot,
    }
    return render(request, 'folio/index.html', context)