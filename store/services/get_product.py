from django.http import Http404
from django.shortcuts import get_object_or_404
from store.models import Product, Characteristics


def get_product_by_slug(slug):
    try:
        return get_object_or_404(Product, slug=slug)
    except Product.DoesNotExist:
        raise Http404(f"Product with slug {slug} not found...")


def get_products_by_category(category_):
    try:
        return Product.objects.filter(category=category_)
    except Product.DoesNotExist:
        raise Http404(f"Product with category {category_.name} not found...")


def get_product_characteristics_by_slug(product):
    try:
        return Characteristics.objects.get(product=product)
    except Product.DoesNotExist:
        raise Http404(f"Characteristics for Product {product} not found...")

