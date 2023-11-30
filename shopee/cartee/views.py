from django.shortcuts import render
from .models import Product, Cart
from django.http import JsonResponse
# Create your views here.


def store(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity' : 0}
    products = Product.objects.all()
    context = {'products':products, 'cart':cart, 'cartitems': cartitems}
    return render(request, 'cartee/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity' : 0}
    context = {'cart':cart, 'cartitems': cartitems}
    return render(request, 'cartee/cart.html', context)

def updateCart(request):
    return JsonResponse('')
