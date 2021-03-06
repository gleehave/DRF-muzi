from rest_framework             import generics, status
from rest_framework.generics    import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response    import Response

from accounts.serializers import UserSerializer, SignInSerializer
from core.querydebugger   import query_debugger



class SignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class SignInView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignInSerializer

    @query_debugger
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({
            "token": token.key,
            "email": request.data['email']
        }, status=status.HTTP_200_OK)