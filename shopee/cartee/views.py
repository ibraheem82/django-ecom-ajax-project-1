from django.shortcuts import render
from .models import Product
# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'cartee/store.html', context)


def cart(request):
    context = {}
    return render(request, 'cartee/cart.html', context)
