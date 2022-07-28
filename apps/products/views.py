from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/_list.html'
    context_object_name = 'products'


class ProductNewView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/_new.html'
