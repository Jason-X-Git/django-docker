from django.urls import path

from products.views import OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='orders')
]
