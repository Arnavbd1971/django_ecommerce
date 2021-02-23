from django.shortcuts import render
from .cart import Cart

def cartPage(request):
    cart = Cart(request)
    print(cart)

    context = {
        'cart':cart
    }
    return render(request, 'cart.html', context)
