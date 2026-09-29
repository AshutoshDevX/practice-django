from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Shop home page')

def products(request):
    return HttpResponse('Shop products page')

def shop_list(request):
    return render(request,'shop/shop_list.html')