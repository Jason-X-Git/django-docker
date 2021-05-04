from django.shortcuts import render
from django.views.generic import ListView
from .models import Order

# Create your views here.

class OrderListView(ListView):
    template_name = 'products/orders.html'
    model = Order
    
    def get_queryset(self):
        return super().get_queryset()
