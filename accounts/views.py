from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from accounts.serializers import UserSerializer, SignInSerializer


class SignUpAPIView(CreateAPIView):
    serializer_class = UserSerializer

class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({
            "token": token.key
        }, status=status.HTTP_200_OK)