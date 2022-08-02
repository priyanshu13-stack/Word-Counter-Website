from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Priyanshu'
    feature1.details = 'Our service is very quick'
    return render(request,'index.html',{'feature' : feature1})

def counter(request):
    text = request.POST['text']
    amt = len(text.split())
    return render(request,'counter.html',{'amount':amt})