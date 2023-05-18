import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from .models import Cart
from .models import CartItem
from .services.get_product import *


def index(request):
    return render(request, 'store/index.html')


# def category(request, category_slug):
#     return render(request, 'store/category_page.html')


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


"""
def get_product_featuress(request, slug_id):
    ip = get_client_ip(request)
    content = {
        "product": get_special_product(slug_id),
        "cart": get_cart_by_user(ip),
        "characteristic": get_characteristic_by_product(get_special_product(slug_id)),
    }
    return render(request, "store/get_product_featuress.html", context=content)



def get_all_product_details(request, slug_id):

    ip = get_client_ip(request)
    liked = check_if_post_like_and_get_count(slug_id, request.user)

    add_view_of_post(request, get_special_product(slug_id))
    content = {
        "product": get_special_product(slug_id),
        "image": get_all_aditional_image_by_slug_id(slug_id),
        "header_menu": get_header_menu(),
        "special_menu_function": "All about the product",
        "special_dict_menu": get_dict_aditional_like(
            request.user, get_list_of_special(get_special_product(slug_id))
        ),
        "is_liked": liked,
        "cart": get_cart_by_user(ip),
    }

    return render(request, "store/get_more.html", context=content)

"""

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
