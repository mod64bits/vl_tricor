from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField('Cliente Nome', max_length=50)
    doc = models.CharField('CPF/CNPJ', max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer:customer_list")
