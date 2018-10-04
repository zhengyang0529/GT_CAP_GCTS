from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('HOme page')
