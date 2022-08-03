from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('Produto', max_length=50)
    price = models.DecimalField('Valor', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:product_list")
