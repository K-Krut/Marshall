from django.shortcuts import render
from .models import Product

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


# def product(request, product_slug):
#     return render(request, 'store/product.html')
