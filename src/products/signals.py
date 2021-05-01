from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from .models import Product

@receiver([post_save,post_delete])
def save_product(sender, instance, **kwargs):
    if sender is Product:
        signal = kwargs.get('signal')
        # print(f'{sender} is sending !')
        # print(f'{instance} received signal: {signal}')
        # if signal is post_delete:
            # print(f'{instance} is deleted !!!!!!!!')
        # if signal is post:
            # print(f'{instance} saved !!!!!!!!!!!!!!')