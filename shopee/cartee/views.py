from django.shortcuts import render
from .models import Product, Cart
# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'cartee/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
    context = {'cart':cart, 'cartitems': cartitems}
    return render(request, 'cartee/cart.html', context)
