from rest_framework             import generics
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny

from core.querydebugger import query_debugger
from products.models      import Product
from products.serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    @query_debugger
    def get_queryset(self):
        types_id = self.kwargs['types_id']
        return Product.objects.filter(type_id=types_id)

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = ['pk']

    @query_debugger
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj