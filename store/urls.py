from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('headphones', views.headphones, name='headphones'),
                  path('catalog', views.catalog, name='catalog'),
                  path('accessories', views.accessories, name='accessories'),
                  path('acoustic', views.acoustic, name='acoustic'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
