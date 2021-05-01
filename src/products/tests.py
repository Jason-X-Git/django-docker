from django.test import TestCase
from .models import Product

# models test


class ProductTest(TestCase):

    def create_product(self, name="TV", price=500):
        return Product.objects.create(name=name, price=price)

    def test_product_creation(self):
        p = self.create_product()
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(p.price, 500)
