from rest_framework             import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response
from rest_framework.views       import APIView

from carts.models        import Cart
from carts.serializers   import CartSerializer
from core.logindecorator import login_decorator
from core.querydebugger  import query_debugger


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @login_decorator
    @query_debugger
    def post(self, request):
        pass

    @login_decorator
    @query_debugger
    def get(self, request):
        try:
            user_id = request.user.id
            cart = Cart.objects.filter(user_id=user_id)
            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({
                'error': "Cart_does_not_exist"
            }, status=status.HTTP_400_BAD_REQUEST)

    @login_decorator
    def put(self, request):
        pass

    @login_decorator
    def delete(self, request):
        pass

