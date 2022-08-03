from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.detail import DetailView
from .models import CartItem
from apps.products.models import Product
from apps.customers.models import Customer
from .models import Order


class CreateCarditemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso')
        return reverse('product:product_list')


class CartItemView(TemplateView):
    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0, min_num=0, max_num=100
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        context['clientes'] = Customer.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            self.request.session['KEY_CUSTOMER'] = request.POST['select-cliente']

            if self.request.POST['venda']:
                messages.success(request, 'Compra Realizada com sucesso!')
                return HttpResponseRedirect(reverse('checkout:checkout'))
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)


class CheckoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'checkout:order'
    def get_redirect_url(self, *args, **kwargs):
        session_key = self.request.session.session_key
        customer_key = self.request.session['KEY_CUSTOMER']
        customer = Customer.objects.get(pk=int(customer_key))
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(
                customer=customer, cart_items=cart_items
            )
            order.save()
            kwargs['pk'] = order.id
            messages.success(self.request, 'Produto atualizado com sucesso')
            return super().get_redirect_url(*args, **kwargs)
        else:
            messages.info(self.request, 'Não há itens no carrinho de compras')
            return redirect('checkout:cart_item')


class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'checkout/order_detail.html'
