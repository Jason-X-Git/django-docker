from customers.models import Customer
from django.db import models
from django.db.models.fields.related import ForeignKey
from uuid import uuid1
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
    orderID = models.UUIDField(default=uuid1)
    customer = ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL,
                          null=True)
    products = models.ManyToManyField(Product, related_name='orders', through='OrderAmount')
    order_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.customer or "Anonymous"} - Products: {self.products.count()} - {self.products.all()}'
    


class OrderAmount(models.Model):
    product = ForeignKey(Product, related_name='order_amounts',
                         on_delete=models.CASCADE)
    order = ForeignKey(Order, related_name='order_amounts', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.product} - {self.amount} - {self.order.customer or "Anonymous"}'
    
