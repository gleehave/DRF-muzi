from django.urls         import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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