from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.logindecorator import login_decorator


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @login_decorator
    def post(self, request):
        pass

    @login_decorator
    def get(self, request):
        pass

    @login_decorator
    def put(self, request):
        pass

    @login_decorator
    def delete(self, request):
        pass

