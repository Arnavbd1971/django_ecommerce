from django.shortcuts import render
from apps.stores.models import *

def frontPage(request):
    products = Product.objects.filter(is_featured=True)
    context = {
        'products':products
    }
    return render(request, 'frontpage.html', context)

def contactPage(request):
    return render(request, 'contact.html')

def aboutPage(request):
    return render(request, 'about.html')