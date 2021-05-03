from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Order, ProductAmount
from django.db.models import Sum


@receiver(pre_save)
def save_product(sender, instance, **kwargs):
    if sender is ProductAmount:
        print('Sending is ProductAmount')
        # print(instance.order.total_cost)
        # instance.order.total_cost = sum(
            # t.product_cost for t in instance.order.product_amounts.all())
        print(instance.order.total_cost)
    if sender is Order:
        print('Sending is Order')
        # print(instance.total_cost)
        # instance.total_cost = sum(
            # t.product_cost for t in instance.product_amounts.all())
        print(instance.total_cost)

    # print(list(instance.product_amounts))
    # instance.total_price = sum([o.product_cost for o in list(instance.product_amounts)])
    # print(instance.total_price)
    # if sender is Order:
    # signal = kwargs.get('signal')
    # print(f'{sender} is sending !')
    # print(f'{instance} received signal: {signal}')
    # if signal is post_delete:
    # print(f'{instance} is deleted !!!!!!!!')
    # if signal is post:
    # print(f'{instance} saved !!!!!!!!!!!!!!')
