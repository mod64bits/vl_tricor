from django.urls import path, re_path
from .views import CreateCarditemView, CartItemView, CheckoutView, OrderDetailView

app_name = 'checkout'

urlpatterns = [
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('adcionar/<int:pk>/', CreateCarditemView.as_view(), name='add_item'),
    path('venda/', CartItemView.as_view(), name='sales'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]