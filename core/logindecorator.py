from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from accounts.models import User


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            input_token  = request.headers.get('Authorization', None)[6:]
            email        = request.headers.get('email', None)
            user         = User.objects.get(email=email)
            server_token = Token.objects.get(user=user).key

            if input_token == server_token:
                request.user = user
            else:
                raise ValidationError({"error": "Invalid Token"})

        except User.DoesNotExist:
            raise ValidationError({"error": "User_Does_Not_Exist"})

        return func(self, request, *args, **kwargs)
    return wrapper