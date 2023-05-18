from django.shortcuts import render
from .models import Product
from .services.get_product import get_product_by_slug


def index(request):
    return render(request, 'store/index.html')


# def category(request, category_slug):
#     return render(request, 'store/category_page.html')


def products(request):
    queryset = Product.objects.all()
    context = {
        "products": queryset
    }
    return render(request, 'store/products.html', context)


def product(request, product_slug):
    context = {
        "product": get_product_by_slug(product_slug)
    }
    return render(request, 'store/product.html', context)


"""
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
