from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class UserSignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.data.get('email'))
            return Response({"status": 0, "message": "User with this email address already exist, try with"
                                                     "try with different one"})
        except ObjectDoesNotExist as e:
            serialized = SignUpSerializers(data=request.data, context={'context': request}, partial=True)
            if serialized.is_valid():
                # serialized.save()
                return Response({"status": 0, "message": "User has been created"}, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
