from rest_framework                          import serializers
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
    type = serializers.CharField(source='type.name') # many=True 옵션이 안먹는다
    tags = serializers.CharField(source='tags.name') # many=True 옵션이 안먹는다

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')
        # fields = ['type', 'tags']

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
    product = ProductSerializer(read_only=True)
    size    = SizeSerializer(read_only=True)
    color   = ColorSerializer(read_only=True)

    class Meta:
        model = ProductOption
        fields = '__all__'