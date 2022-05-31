from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.models import User
from carts.models import Cart
from products.models import ProductOption

class ProductTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', email='test@example.com', password='test1234@@', is_staff=True)
        self.productoption = ProductOption.objects.create(product_id=1, size_id=1,color_id=1,stock=3)
        self.cart = Cart.objects.create(user_id=self.user.id, quantity=1, product_option=self.productoption.id)

    def test_get_cart_APIView(self):
        response = self.client.get(f'http://127.0.0.1/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
