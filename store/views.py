from django.shortcuts import render

def index(request):
    return render(request, 'store/index.html')


def category(request, category_slug):
    return render(request, 'store/category_page.html')


def categories(request):
    return render(request, 'store/categories.html')


def product(request, product_slug):
    return render(request, 'store/product.html')
