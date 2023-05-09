from store.models import Categories


def get_all_categories():
    return {"categories": Categories.objects.all()}
