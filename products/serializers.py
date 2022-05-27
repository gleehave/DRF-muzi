from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework                          import serializers
from rest_framework.validators               import UniqueValidator
from rest_framework.authtoken.models         import Token
from accounts.models                         import User
from core.querydebugger                      import query_debugger
from products.models import Product, Tag, Type, Category, TagProduct, ProductOption, Size, Color, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    type = TagSerializer(many=True)
    tags = TypeSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

class TagProductSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = TagProduct
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Image
        fields = '__all__'

class ProductOptionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    size = SizeSerializer(many=True)
    color = ColorSerializer(many=True)
    class Meta:
        model = ProductOption
        fields = '__all__'