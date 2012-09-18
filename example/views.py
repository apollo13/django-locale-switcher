from django.http import HttpResponse
from django.shortcuts import render

def home(request, *args, **kwargs):
    return render(request, 'test.html')
