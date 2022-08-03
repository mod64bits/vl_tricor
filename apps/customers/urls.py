from django.urls import path, re_path
from .views import CustomerListView, CustomerNewView

app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('novo/', CustomerNewView.as_view(), name='customer_new'),
]