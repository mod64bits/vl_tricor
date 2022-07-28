from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.home import urls as home_urls
from apps.products import urls as product_uls
from apps.customers import urls as customer_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('home/clientes', include(customer_url)),
    path('home/products', include(product_uls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
