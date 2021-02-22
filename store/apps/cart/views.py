from django.shortcuts import render

def cartPage(request):
    return render(request, 'cart.html')
