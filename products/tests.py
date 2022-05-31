from django.urls         import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from products.models import Product, Type, Category


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

    def test_get_product_list_APIView(self):
        response = self.client.get(f'http://127.0.0.1/product/categories/{self.type.id}/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Product_detail_APIView(self):
        response = self.client.get(f'http://127.0.0.1/product/categories/{self.product.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)