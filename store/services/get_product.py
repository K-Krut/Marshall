from django.http import Http404
from django.shortcuts import get_object_or_404
from store.models import Product


def get_product_by_slug(slug):
    try:
        return get_object_or_404(Product, slug=slug)
    except Product.DoesNotExist:
        raise Http404(f"Product with slug {slug} not found...")
