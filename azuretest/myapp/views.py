from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("this is home page")


def test(request):
    return HttpResponse("This is testing page")