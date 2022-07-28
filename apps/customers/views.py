from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/_list.html'
    context_object_name = 'customers'


class CustomerNewView(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'customers/_new.html'
