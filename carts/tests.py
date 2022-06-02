from rest_framework                  import status
from rest_framework.authtoken.models import Token
from rest_framework.test             import APITestCase

from accounts.models import User
from carts.models    import Cart
from products.models import ProductOption, Category, Product, Type, Size, Color


class ProductTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'test',
            email    = 'test@example.com',
            password = 'test1234@@',
        )
        self.token    = Token.objects.create(user=self.user)
        self.category = Category.objects.create(name='category1')
        self.type     = Type.objects.create(
            name                = 'type1',
            thumbnail_image_url = '1',
            category            = self.category
        )
        self.size     = Size.objects.create(name='size1')
        self.color    = Color.objects.create(name='color1')
        self.product  = Product.objects.create(
            name                = 'product1',
            price               = 1000,
            description         = 'this is product1',
            thumbnail_image_url = 'image1.png',
            type                = self.type
        )
        self.productoption = ProductOption.objects.create(
            product = self.product,
            size    = self.size,
            color   = self.color,
            stock   = 3
        )
        self.cart = Cart.objects.create(
            user           = self.user,
            quantity       = 1,
            product_option = self.productoption
        )

    def test_get_cart_APIView(self):

        header = {
            'HTTP_AUTHORIZATION' : 'Token ' + self.token.key,
            'HTTP_EMAIL'              : self.user.email
        }
        response = self.client.get(f'http://127.0.0.1/cart/', **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
