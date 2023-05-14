from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('products', views.products, name='products'),
                  # path('categories/<slug:category_slug>', views.categories, name='categories'),
                  # path('products/<slug:product_slug>', views.product, name='product'),
                  path('cart/', views.cart, name='cart'),
                  path("add_to_cart", views.add_to_cart, name="add"),
                  # path('cart/remove/<slug:product_slug>', views.remove_from_cart, name='remove_from_cart'),
                  # path('cart/clear', views.clear_cart, name='clear_cart'),
                  # path('search/', search, name='search'),
                  # path('order_complete', order_complete, name='order_complete'),
                  # path('checkout', checkout, name='checkout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
