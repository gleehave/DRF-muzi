from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from core.timestamp import TimeStampedModel


class Wishlist(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    product_option = models.ForeignKey('products.ProductOption', on_delete=models.CASCADE, related_name='wishlist')

    class Meta:
        db_table = 'wishlists'