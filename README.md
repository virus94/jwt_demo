# jwt_demo

Steps: How to use?

1. Create a virtual env for python 3
2. install requirement.txt file in your enviroment with pip3 install -r requirement.txt

For set in your new project:

pip3 install django
pip3 install djangorestframework
pip3 install djangorestframework-jwt

In your settings.py file add:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
}

Now setup your database file

Now in your project app in urls.py file add

from django.urls import path, include

from django.contrib import admin
from .views import *
from rest_framework_jwt.views import *


urlpatterns = [
    path('sign_up/', UserSignUp.as_view(), name="sign_up"),
    path('api-token-auth/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
]


Now your views.py file add

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

In the serializers file add 

class SignUpSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')


Now run the project and the with following urls:

127.0.0.1:8000/sign_up/

with payload
{
	"email": "",
	"password": ""
}

127.0.0.1:8000/api-token-auth/

with payload

{
	"username": "",
	"password": ""
}


127.0.0.1:8000/auth-jwt-verify/

with payload
{
	"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTU0ODg1NTY3LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTU0ODg1MjY3fQ.NBalBJV59N0yahpMsMTZmQ9PzuL-l2bXX7DJlM2yLFg"
}


127.0.0.1:8000/auth-jwt-refresh/
with payload

{
	"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTU0ODg1NTY3LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTU0ODg1MjY3fQ.NBalBJV59N0yahpMsMTZmQ9PzuL-l2bXX7DJlM2yLFg"
}





