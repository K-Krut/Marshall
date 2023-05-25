from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('products', views.products, name='products'),
                  # path('categories', views.categories, name='categories'),
                  path('categories/<slug:category_slug>', views.category, name='category_page'),
                  path('products/<slug:product_slug>', views.product, name='product_details'),
                  path('cart/', views.cart, name='cart'),
                  path("add_to_cart", views.add_to_cart, name="add"),
                  # path('cart/remove/<slug:product_slug>', views.remove_from_cart, name='remove_from_cart'),
                  path('cart/clear', views.clear_cart, name='clear_cart'),
                  path('search/', views.search_product, name='search_product'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
