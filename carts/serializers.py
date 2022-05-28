from rest_framework       import serializers
from accounts.serializers import UserSerializer
from products.serializers import ProductOptionSerializer

from carts.models         import Cart

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer
    product_option = ProductOptionSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
