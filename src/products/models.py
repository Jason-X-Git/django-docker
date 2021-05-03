from customers.models import Customer
from django.db import models
from django.db.models.fields.related import ForeignKey
from uuid import uuid1
from django.db.models import Sum

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products', default='no_pickure.gif')
    price = models.FloatField(help_text='in US dollars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ${self.price}'


class Order(models.Model):
    orderID = models.UUIDField(default=uuid1, editable=False)
    customer = ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL,
                          null=True)
    products = models.ManyToManyField(
        Product, related_name='orders', through='ProductAmount')
    # total_cost = models.FloatField(
        # help_text='in US dollars', default=0, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer or "Anonymous"} - ${self.total_cost:.2f} \
    - Products: {", ".join(f"{p.product.name} {p.amount}" for p in self.product_amounts.all())}'
    # - Products: {", ".join(list(self.products.order_by().values_list("name", flat=True).distinct()))}'
        # return f'{self.customer or "Anonymous"} - Products: {self.products.count()} - {self.products.all()}'
    @property
    def total_cost(self):
        return sum(
            t.product_cost for t in self.product_amounts.all())

class ProductAmount(models.Model):
    product = ForeignKey(Product, related_name='product_amounts',
                         on_delete=models.CASCADE)
    order = ForeignKey(Order, related_name='product_amounts',
                       on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - {self.amount} - {self.product_cost} - {self.order.customer or "Anonymous"} - {self.order.orderID}'

    @property
    def product_cost(self):
        return self.product.price * self.amount
