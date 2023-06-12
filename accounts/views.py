from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import get_user_model

from . import serializers


# Create your views here.


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'id': user.id,
                'email': user.email,
                'first_name': user.full_name,
                'token': f"Token {Token.objects.get_or_create(user=user)[0].key}"
            })
        return Response({'error': 'Invalid credentials'})


class RegisterAPIView(APIView):
    serializer_class = serializers.UserRegisterSerializer

    @swagger_auto_schema(
        operation_description="Registration user",
        request_body=openapi.Schema(
            required=['first_name', 'last_name',
                      'email', 'password', 'password2'],
            type=openapi.TYPE_OBJECT,
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description="First name"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description="Last name"),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="User registration",
                examples={
                    'application/json': {
                            'id': 11,
                            'first_name': 'Palonchi',
                            'last_name': 'Palonchiyev',
                            'email': 'palonchi@gmail.com',
                            "password": "oylaizlatop",
                            "password2": "oylaizlatop"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                            'error': 'Invalid credentials'
                    }
                }
            )
        }
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetailAPIView(generics.RetrieveAPIView):
    queryset = get_user_model()
    serializer_class = serializers.UserRegisterSerializer
