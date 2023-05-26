from django.http import Http404
from django.shortcuts import get_object_or_404
from store.models import Categories


def get_category_by_slug(slug):
    try:
        return get_object_or_404(Categories, slug=slug)
    except Categories.DoesNotExist:
        raise Http404(f"Product with slug {slug} not found...")
