from django.urls                     import reverse
from rest_framework                  import status
from rest_framework.authtoken.models import Token
from rest_framework.test             import APITestCase

from accounts.models import User


class SignUpTestCase(APITestCase):
    def test_post_signup(self):
        data = {
            "username"    : "testuser",
            "email"       : "test@example.com",
            "password"    : "password##1234",
            "phone_number":"010-111-1111"
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class SignInTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password##123')
        self.token = Token.objects.create(user=self.user)

    def test_post_signin(self):
        data = {
            "username"    : "testuser",
            "email"       : "test@example.com",
            "password"    : "password##123",
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)