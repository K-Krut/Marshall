from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
              ]
"""

    path('categories/', views.categories, name='categories'),  # HTTP response code: 200 (OK)
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),  # HTTP response code: 200 (OK) or 404 (Not Found)
    path('products/', views.products, name='products'),  # HTTP response code: 200 (OK)
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  # HTTP response code: 200 (OK) or 404 (Not Found)
    path('login/', views.login, name='login'),  # HTTP response code: 200 (OK) or 302 (Redirect)
    path('logout/', views.logout, name='logout'),  # HTTP response code: 302 (Redirect)
    path('register/', views.register, name='register'),  # HTTP response code: 200 (OK) or 302 (Redirect)
    path('cart/', views.cart, name='cart'),  # HTTP response code: 200 (OK)
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # HTTP response code: 302 (Redirect)
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # HTTP response code: 302 (Redirect)
    path('cart/clear/', views.clear_cart, name='clear_cart'),  # HTTP response code: 302 (Redirect)
"""