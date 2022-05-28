from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views       import APIView

from carts.models import Cart
from carts.serializers   import CartSerializer
from core.logindecorator import login_decorator


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @login_decorator
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @login_decorator
    def get(self, request):
        try:
            user_id = request.user.id
            print('\n')
            print("user_id: ", user_id)
            cart = Cart.objects.get(user_id=user_id)
            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'error': "Cart_does_not_exist"}, status=status.HTTP_400_BAD_REQUEST)

    @login_decorator
    def put(self, request):
        pass

    @login_decorator
    def delete(self, request):
        pass

