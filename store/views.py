import json

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from . import models
from .models import Product
from .models import Cart
from .models import CartItem
from .services.get_product import *


def index(request):
    return render(request, 'store/index.html')


def products(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        context = {"products": products, "cart": cart}
        return render(request, "store/products.html", context)

    context = {
        "products": products
    }
    return render(request, 'store/products.html', context)


def product(request, product_slug):
    context = {
        "product": get_product_by_slug(product_slug),
        "characteristics": get_product_characteristics_by_slug(get_product_by_slug(product_slug))
    }
    return render(request, 'store/product.html', context)


def cart(request):
    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    context = {"cart": cart, "items": cartitems}
    return render(request, "store/cart.html", context)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()

    return JsonResponse(product_id, safe=False)

def remove_from_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if cartitem.quantity > 0:
            cartitem.quantity -= 1
        cartitem.save()

    return JsonResponse(product_id, safe=False)


def clear_cart(request):
    user = request.user
    CartItem.objects.filter(cart__user=user).delete()
    Cart.objects.filter(user=user).delete()
    return HttpResponseRedirect(reverse("cart"))


def search_product(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'store/products_search.html', {"results": results})

    return render(request, 'store/products_search.html')
