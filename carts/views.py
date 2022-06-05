from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response
from rest_framework.views       import APIView

from carts.models        import Cart
from carts.serializers import GETCartSerializer, POSTCartSerializer
from core.logindecorator import login_decorator
from core.querydebugger  import query_debugger
from products.models import ProductOption, Product, Size, Color
from products.serializers import ProductOptionSerializer


class CartAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    @login_decorator
    @query_debugger
    def post(self, request):
        try:
            serializer = POSTCartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(serializer.errors)

    @login_decorator
    @query_debugger
    def get(self, request):
        try:
            user_id = request.user.id
            cart = Cart.objects.filter(user_id=user_id)
            serializer = GETCartSerializer(cart, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({
                'error': "Cart_does_not_exist"
            }, status=status.HTTP_400_BAD_REQUEST)

    @login_decorator
    def delete(self, request):
        pass

