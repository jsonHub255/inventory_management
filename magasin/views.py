from django.http import HttpResponse
from django.shortcuts import render
from .models import Designation, Engin


# Create your views here.
def index(request):
    desi = Designation.objects.all()
    return render(request, "magasin/index.html", {
        "desi": desi
    })