from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

def login(request):
    return render(request,'form/login.html')
