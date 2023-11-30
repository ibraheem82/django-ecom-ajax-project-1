from django.shortcuts import render
from .models import Product, Cart, CartItems
from django.http import JsonResponse
import json
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
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    # Get the product by its ID
    product = Product.objects.get(product_id = product_id)
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed = False)
        cartitems, created = CartItems.objects.get_or_create(product = product, cart = cart)

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()
    # Get the name of the product
        product_name = product.name
        return JsonResponse({'message': 'It is working', 'product_name': product_name}, safe=False)
    else:
        return JsonResponse({'message': 'User is not authenticated'}, safe=False)
