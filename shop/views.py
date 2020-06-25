from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request ,'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('contact')



def tracker(request):
    return HttpResponse('tracker')



def search(request):
    return HttpResponse('search')


def productView(request):
    return HttpResponse('prodView')


def checkout(request):
    return HttpResponse('checkout')