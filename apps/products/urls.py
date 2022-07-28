from django.urls import path, re_path
from .views import ProductListView, ProductNewView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('/novo/', ProductNewView.as_view(), name='product_new'),
]