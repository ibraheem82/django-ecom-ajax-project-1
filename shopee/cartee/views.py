from django.shortcuts import render

# Create your views here.


def store(request){
    context = {}
    return render(request, 'cartee/store.html', context)
}

def cart(request){
    context = {}
    return render(request, 'cartee/cart.html', context)
}