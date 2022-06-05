from rest_framework       import serializers
from accounts.serializers import UserSerializer
from products.serializers import ProductOptionSerializer

from carts.models         import Cart

class GETCartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product_option = ProductOptionSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'quantity', 'user', 'product_option')

class POSTCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"