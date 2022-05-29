from django.urls         import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from products.models import Product, Type, Category, Tag


class ProductTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='category1')
        self.type = Type.objects.create(name='type1', thumbnail_image_url='1', category=self.category)
        self.product = Product.objects.create(
            name = 'product1',
            price = 1000,
            description = 'this is product1',
            thumbnail_image_url = 'image1.png',
            type = self.type
        )

    def test_get_product_list_apiview(self):
        pass