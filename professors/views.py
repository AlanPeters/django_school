from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def professors(request):
    return HttpResponse("Professosrs")
