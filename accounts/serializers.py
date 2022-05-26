from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework                          import serializers
from rest_framework.validators               import UniqueValidator
from rest_framework.authtoken.models         import Token
from accounts.models                         import User

class UserSerializer(serializers.Serializer):
    email        = serializers.EmailField(max_length=200, validators=[UniqueValidator(queryset=User.objects.all())])
    password     = serializers.CharField(validators=[validate_password], write_only=True)
    username     = serializers.CharField(max_length=254, write_only=True)
    phone_number = serializers.CharField(max_length=50, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class SignInSerializer(serializers.Serializer):
    email        = serializers.EmailField(max_length=200, required=True)
    password     = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError({
            "error": "Unable to sign in with provided credentials."
        })