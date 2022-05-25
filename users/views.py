from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class SignUpAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):


        return Response(serializer.data, status=status.HTTP_201_CREATED)

