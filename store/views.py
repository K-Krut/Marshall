from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html')


def catalog(request):
    return render(request, 'store/catalog.html')


def headphones(request):
    return render(request, 'store/category_page.html')


def acoustic(request):
    return render(request, 'store/category_page.html')


def accessories(request):
    return render(request, 'store/category_page.html')


def product(request):
    return render(request, 'store/product.html')
